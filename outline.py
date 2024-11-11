from outlines.function import Function

def function_call_example(content):
    # Define a function using `Function` to analyze the text
    analyze_text = Function(
        lambda content: f"Analysis: {content}",
        input_type=str,
        output_type=str
    )

    # Call the function with the provided content
    return analyze_text(content)


# Test the function
if __name__ == "__main__":
    content = "This is a sample research paper content."
    result = function_call_example(content)
    print(result)
