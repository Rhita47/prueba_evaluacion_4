import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

# Jeroglíficos y sus frecuencias
symbols = {
    'Sphinx': 5,
    'Pyramid': 7,
    'Lotus': 8,
    'Scarab': 9,
    'Obelisk': 10,
    'Djed': 11,
    'Eye of Horus': 12,
    'Ankh': 15
}

# Crear una cola de prioridad
priority_queue = [Node(sym, freq) for sym, freq in symbols.items()]
heapq.heapify(priority_queue)

# Función para construir el árbol de Huffman
def build_huffman_tree():
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(priority_queue, merged)

    return priority_queue[0]

# Construir el árbol
root = build_huffman_tree()

# Función para generar los códigos Huffman
def generate_codes(node, code="", codes={}):
    if node.char:
        codes[node.char] = code
    else:
        generate_codes(node.left, code + "0", codes)
        generate_codes(node.right, code + "1", codes)
    return codes

# Generar los códigos Huffman
huffman_codes = generate_codes(root)

# Función para descifrar el mensaje
def decode(encoded_message, codes):
    reverse_codes = {v: k for k, v in codes.items()}
    decoded_message = []
    buffer = ""
    for bit in encoded_message:
        buffer += bit
        if buffer in reverse_codes:
            decoded_message.append(reverse_codes[buffer])
            buffer = ""
    return decoded_message

# Mensajes codificados
encoded_messages = [
    "10001011101011000010111010001110000011011000000111100111101001011000011010011100110100010111010111111101000011110011111100111101000110001100000010110101111011111110111010110110111001110110111100111111100101001010010100000101101011000101100110100011100100101100001100100011010110101011111111111011011101110010000100101011000111111100010001110110011001011010001101111101011010001101110000000111001001010100011111100001100101101011100110011110100011000110000001011010111110011100",
    "0110101011011100101000111101011100110111010110110100001000111010100101111010011111110111001010001111010111001101110101100001100010011010001110010010001100010110011001110010010000111101111010"
]

# Descifrar mensajes
decoded_messages = [decode(msg, huffman_codes) for msg in encoded_messages]

# Calcular espacio de memoria
original_bits = sum(symbols[sym] * 8 for sym in symbols)  # 8 bits por símbolo
compressed_bits = sum(len(huffman_codes[sym]) * symbols[sym] for sym in symbols)

print("Códigos Huffman:", huffman_codes)
print("Mensaje 1 descifrado:", decoded_messages[0])
print("Mensaje 2 descifrado:", decoded_messages[1])
print("Espacio original estimado (en bits):", original_bits)
print("Espacio comprimido (en bits):", compressed_bits)
# Códigos Huffman generados previamente (pueden variar si el árbol es reconstruido)
huffman_codes = {
    'Ankh': '00',
    'Lotus': '010',
    'Scarab': '011',
    'Obelisk': '100',
    'Djed': '101',
    'Sphinx': '1100',
    'Pyramid': '1101',
    'Eye of Horus': '111'
}

# Función para decodificar un mensaje codificado usando códigos Huffman
def decode(encoded_message, codes):
    reverse_codes = {v: k for k, v in codes.items()}
    decoded_message = []
    buffer = ""
    for bit in encoded_message:
        buffer += bit
        if buffer in reverse_codes:
            decoded_message.append(reverse_codes[buffer])
            buffer = ""
    return decoded_message

# Mensajes codificados proporcionados
encoded_messages = [
    "10001011101011000010111010001110000011011000000111100111101001011000011010011100110100010111010111111101000011110011111100111101000110001100000010110101111011111110111010110110111001110110111100111111100101001010010100000101101011000101100110100011100100101100001100100011010110101011111111111011011101110010000100101011000111111100010001110110011001011010001101111101011010001101110000000111001001010100011111100001100101101011100110011110100011000110000001011010111110011100",
    "0110101011011100101000111101011100110111010110110100001000111010100101111010011110111001010001111010111001101110101100001100010011010001110010010001100010110011001110010010000111101111010"
]

# Aplicar la función de descifrado a cada mensaje codificado
decoded_messages = [decode(msg, huffman_codes) for msg in encoded_messages]

# Unir los elementos decodificados para formar el mensaje completo descifrado
decoded_text_messages = [' '.join(message) for message in decoded_messages]

# Imprimir los mensajes descifrados
for i, message in enumerate(decoded_text_messages, 1):
    print(f"Mensaje {i} descifrado: {message}")

