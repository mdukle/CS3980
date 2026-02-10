def echo(text: str, repetition: int = 3) -> str:
        """Imitate a real-world echo."""
        print(text)
        return text

if __name__ == "__main__":
        text = input("Yell something at a mountain: ")
        print(echo(text), 'from console')