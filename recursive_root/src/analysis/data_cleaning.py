import numpy as np
import pandas as pd

def clean_final_information(final_information):
    final_information_cleaned = {}
    for f in final_information:
        query = f['query']
        snippet = f['snippet']

        unique_query = query
        count = 1
        while unique_query in final_information_cleaned:
            unique_query = f"{query}_{count}"
            count += 1

        final_information_cleaned[unique_query] = snippet

    return final_information_cleaned

def create_qa_context(final_information_cleaned):
    qa_context = pd.DataFrame(final_information_cleaned, index=[0]).T.reset_index()
    qa_context.columns = ['Query', 'Context']
    qa_context['BaseQuery'] = qa_context['Query'].apply(lambda x: x.split('_')[0])
    result_df = qa_context.groupby('BaseQuery', group_keys=False).apply(lambda x: x.sample(1, random_state=np.random.RandomState())).reset_index(drop=True)
    return result_df[['BaseQuery', 'Context']]
