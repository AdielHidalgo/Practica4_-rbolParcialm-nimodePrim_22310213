import sys

class SimuladorPrimConsola:
    def __init__(self, vertices):
        self.V = vertices
        # Inicializamos el grafo como una matriz de adyacencia llena de ceros
        self.grafo = [[0 for columna in range(vertices)] for fila in range(vertices)]

    # Función para encontrar el vértice con el valor de clave mínimo,
    # que aún no está en el Árbol de Expansión Mínima (AEM)
    def min_key(self, key, mst_set):
        min_val = sys.maxsize
        min_index = -1
        for v in range(self.V):
            if key[v] < min_val and not mst_set[v]:
                min_val = key[v]
                min_index = v
        return min_index

    # Función principal para construir y mostrar el AEM
    def prim_aem(self):
        # Almacena el AEM construido
        parent = [None] * self.V
        # Valores clave usados para elegir la arista de peso mínimo
        key = [sys.maxsize] * self.V
        # El primer vértice es la raíz, por lo que su clave es 0
        key[0] = 0
        # Conjunto para rastrear los vértices incluidos en el AEM
        mst_set = [False] * self.V
        
        # El primer nodo no tiene padre
        parent[0] = -1  

        print("Iniciando Algoritmo de Prim...\n")
        
        # El AEM tendrá V vértices
        for _ in range(self.V):
            # 1. Elige el vértice con la clave mínima que no esté en el AEM
            u = self.min_key(key, mst_set)
            
            # 2. Agrega el vértice elegido al conjunto del AEM
            mst_set[u] = True
            
            if parent[u] != -1: # Si no es el nodo inicial
                print(f"Paso {_ + 1}: Vértice {u} incluido en el árbol. Se agrega la arista {parent[u]}-{u} con peso {self.grafo[u][parent[u]]}")
            else:
                print(f"Paso {_ + 1}: Vértice {u} incluido en el árbol (Nodo inicial).")

            # 3. Actualiza los valores de `key` de los vértices adyacentes al vértice elegido.
            # Considera solo los vértices que no están todavía en el AEM.
            for v in range(self.V):
                # graph[u][v] es diferente de 0 solo para vértices adyacentes
                # mst_set[v] es falso para vértices que no están en el AEM
                # Actualiza la clave solo si el peso del grafo es menor que la clave actual
                if self.grafo[u][v] > 0 and not mst_set[v] and key[v] > self.grafo[u][v]:
                    key[v] = self.grafo[u][v]
                    parent[v] = u
        
        self.imprimir_aem(parent)

    def imprimir_aem(self, parent):
        print("\n--- Simulación Finalizada ---")
        print("Árbol de Expansión Mínima (AEM) resultante:")
        print("Arista \tPeso")
        total_cost = 0
        for i in range(1, self.V):
            costo = self.grafo[i][parent[i]]
            total_cost += costo
            print(f"{parent[i]} - {i}\t{costo}")
        print(f"\nCosto total del AEM: {total_cost}")

# --- Ejemplo de Uso ---
if __name__ == '__main__':
    # Creamos un simulador para un grafo con 5 vértices
    s = SimuladorPrimConsola(5)
    
    # Definimos las conexiones y sus pesos (matriz de adyacencia)
    # Un 0 significa que no hay conexión directa
    s.grafo = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0]
    ]

    s.prim_aem()