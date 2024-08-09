import pandas as pd

# Load the CSV files
interactions_file_path = r'ethereum/20150701.csv'
user_data_file_path = r'ethereum/user_data.csv'

interactions_df = pd.read_csv(interactions_file_path)
user_data_df = pd.read_csv(user_data_file_path)

# Convert 'text' column to lowercase for case insensitive search
interactions_df['text'] = interactions_df['text'].str.lower()

# Filter interactions to find authors who used the word "ethereum"
filtered_interactions_df = interactions_df[interactions_df['text'].str.contains('ethereum')]

# Drop NaN values and convert 'author_id' to integers
filtered_interactions_df = filtered_interactions_df.dropna(subset=['author_id'])
filtered_interactions_df['author_id'] = filtered_interactions_df['author_id'].astype(int)

# Get unique author IDs from interactions
interaction_author_ids = filtered_interactions_df['author_id'].unique()

# Get author IDs from user data
user_data_author_ids = user_data_df['author_id'].unique()

# Identify bot IDs (author IDs in interactions but not in user data)
bot_ids = set(interaction_author_ids) - set(user_data_author_ids)

# Identify common IDs (author IDs in both interactions and user data)
common_ids = set(interaction_author_ids) & set(user_data_author_ids)


# Get author IDs and followers count from user data
user_data_subset = user_data_df[user_data_df['author_id'].isin(common_ids)]
author_followers = user_data_subset.groupby('author_id')['followers_count'].sum().astype(int) 



def coefficient_ethereum():
    # Calculate total followers count
    total_followers = author_followers.sum()

    # Calculate total number of interactions containing "ethereum"
    total_interactions = len(interaction_author_ids)

    # Calculate the maximum potential interactions
    max_potential_interactions = len(common_ids) + total_followers

    # Calculate engagement coefficient for the topic "ethereum"
    if total_followers > 0:
        engagement_coefficient = total_interactions / max_potential_interactions
    else:
        engagement_coefficient = 0  # Handle case where there are no author followers

    # Print engagement coefficient
    print(f'\nTotal Interactions : {total_interactions}')
    print(f'\nMax Potential Interactions : {max_potential_interactions}')
    print(f'\nOverall engagement coefficient for the topic "ethereum": {engagement_coefficient:.8f}')

    return engagement_coefficient

if __name__ == "__main__":
    coefficient_ethereum()
