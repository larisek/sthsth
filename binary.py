def binary_to_decimal(binary: str) -> int:
	if not binary or any(bit not in "01" for bit in binary):
		raise ValueError("Binární číslo může obsahovat pouze 0 a 1.")
	return int(binary, 2)


def decimal_to_binary(decimal: str) -> str:
	if not decimal or not decimal.isascii() or not decimal.isdigit():
		raise ValueError("Zadejte nezáporné celé číslo v desítkové soustavě.")
	return format(int(decimal), "b")


def main() -> None:
	print("Převodník číselných soustav")
	print("1. Z binární do desítkové")
	print("2. Z desítkové do binární")

	choice = input("Vyberte převod (1/2): ").strip()

	try:
		if choice == "1":
			number = input("Zadejte binární číslo: ").strip()
			print(f"Desítkové číslo: {binary_to_decimal(number)}")
		elif choice == "2":
			number = input("Zadejte nezáporné celé desítkové číslo: ").strip()
			print(f"Binární číslo: {decimal_to_binary(number)}")
		else:
			print("Neplatná volba. Vyberte 1 nebo 2.")
	except ValueError as error:
		print(f"Chyba: {error}")


if __name__ == "__main__":
	main()
