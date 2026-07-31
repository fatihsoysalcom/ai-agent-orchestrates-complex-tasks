class MarketingAgent:
    def __init__(self):
        self.context = {}

    def _skill_product_research(self, product_name):
        """Simulates a skill to research product details and store in context."""
        print(f"  Skill: Researching product '{product_name}'...")
        # Simulate gathering product features and benefits
        if "AI Assistant" in product_name:
            self.context['product_details'] = {
                'name': product_name,
                'features': ['AI-powered', 'natural language processing', 'task automation'],
                'benefits': ['increased productivity', 'time-saving', 'intelligent assistance']
            }
        elif "To-Do App" in product_name:
            self.context['product_details'] = {
                'name': product_name,
                'features': ['simple interface', 'cross-platform sync', 'reminders'],
                'benefits': ['better organization', 'reduced stress', 'goal achievement']
            }
        else:
            self.context['product_details'] = {
                'name': product_name,
                'features': ['basic functionality'],
                'benefits': ['general utility']
            }
        return f"Product '{product_name}' details gathered."

    def _skill_identify_audience(self):
        """Simulates a skill to identify the target audience based on product details in context."""
        print("  Skill: Identifying target audience...")
        product_details = self.context.get('product_details', {})
        features = product_details.get('features', [])

        if 'AI-powered' in features or 'natural language processing' in features:
            self.context['target_audience'] = 'Tech professionals, business leaders, innovators'
        elif 'simple interface' in features or 'cross-platform sync' in features:
            self.context['target_audience'] = 'Students, busy professionals, anyone needing organization'
        else:
            self.context['target_audience'] = 'General public'
        return f"Target audience identified: {self.context['target_audience']}."

    def _skill_generate_marketing_copy(self):
        """Simulates a skill to generate marketing copy using gathered info from context."""
        print("  Skill: Generating marketing copy...")
        product_name = self.context.get('product_details', {}).get('name', 'Our New Product')
        benefits = self.context.get('product_details', {}).get('benefits', [])
        audience = self.context.get('target_audience', 'our valued customers')

        copy = (
            f"Introducing {product_name}! Designed for {audience}, "
            f"it offers {', '.join(benefits)}. "
            "Transform your workflow and achieve more today!"
        )
        self.context['marketing_copy'] = copy
        return "Marketing copy generated."

    def _skill_suggest_channels(self):
        """Simulates a skill to suggest marketing channels based on audience in context."""
        print("  Skill: Suggesting marketing channels...")
        audience = self.context.get('target_audience', 'general public')
        channels = []

        if 'Tech professionals' in audience or 'business leaders' in audience:
            channels.extend(['LinkedIn', 'Industry Webinars', 'Tech Blogs'])
        if 'Students' in audience or 'busy professionals' in audience:
            channels.extend(['Instagram', 'Facebook Ads', 'Productivity Blogs'])
        if not channels:
            channels.append('General Social Media')

        self.context['suggested_channels'] = channels
        return "Marketing channels suggested."

    def orchestrate_task(self, task_description):
        """
        This is the core 'agent' function that orchestrates different skills.
        It acts like a project manager, deciding which skills to invoke and in what order,
        passing information (context) between them to complete a complex task.
        """
        print(f"\nAgent: Received complex task: '{task_description}'")
        self.context = {} # Reset context for a new task

        if "plan a marketing campaign" in task_description.lower():
            # The agent breaks down the complex task into sub-tasks (skills)
            # and executes them sequentially, using the shared 'context'.
            product_name = task_description.split("for ")[-1].strip().replace(".", "")
            print(f"Agent: Orchestrating marketing campaign for '{product_name}'...")

            # Step 1: Research the product (skill invocation)
            result1 = self._skill_product_research(product_name)
            print(f"  Result: {result1}")

            # Step 2: Identify the target audience (skill invocation, uses context from Step 1)
            result2 = self._skill_identify_audience()
            print(f"  Result: {result2}")

            # Step 3: Generate marketing copy (skill invocation, uses context from Steps 1 & 2)
            result3 = self._skill_generate_marketing_copy()
            print(f"  Result: {result3}")

            # Step 4: Suggest channels (skill invocation, uses context from Step 2)
            result4 = self._skill_suggest_channels()
            print(f"  Result: {result4}")

            print("\nAgent: Task completed. Final Campaign Summary:")
            print(f"  Product: {self.context.get('product_details', {}).get('name')}")
            print(f"  Target Audience: {self.context.get('target_audience')}")
            print(f"  Marketing Copy: {self.context.get('marketing_copy')}")
            print(f"  Suggested Channels: {', '.join(self.context.get('suggested_channels', []))}")
            return self.context

        elif "summarize a document" in task_description.lower():
            print("Agent: This agent does not currently have the 'summarize document' skill.")
            return {"status": "skill_not_implemented"}
        else:
            print("Agent: I don't understand this task or don't have the necessary skills.")
            return {"status": "task_unrecognized"}

if __name__ == "__main__":
    agent = MarketingAgent()

    # Example 1: A complex task requiring orchestration of multiple skills
    print("="*50)
    agent.orchestrate_task("Plan a marketing campaign for a new AI Assistant product.")
    print("="*50)

    # Example 2: Another complex task, demonstrating adaptability based on product
    print("\n" + "="*50)
    agent.orchestrate_task("Plan a marketing campaign for a simple To-Do App.")
    print("="*50)

    # Example 3: A task for which the agent lacks a specific skill
    print("\n" + "="*50)
    agent.orchestrate_task("Summarize a document about quantum physics.")
    print("="*50)

    # Example 4: An unrecognized task
    print("\n" + "="*50)
    agent.orchestrate_task("Write a poem about a cat.")
    print("="*50)