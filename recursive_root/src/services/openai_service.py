from openai.lib.azure import AzureOpenAI


class OpenAIService:
    def __init__(self, endpoint, api_key,version, deployment):
        self.client = AzureOpenAI(
            api_version=version,
            azure_endpoint=endpoint,
            api_key=api_key
        )
        self.deployment = deployment

    def generate_response(self, max_tokens,system_prompt,user_prompt):
        if system_prompt:
            response = self.client.chat.completions.create(
                model=self.deployment,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                max_tokens=max_tokens,
                stream=False,
                temperature=0,
            )
        else:
            response = self.client.chat.completions.create(
                model=self.deployment,
                messages=[
                    {"role": "user", "content": user_prompt},
                ],
                max_tokens=max_tokens,
                stream=False,
                temperature=0,
            )
        return response.choices[0].message.content
