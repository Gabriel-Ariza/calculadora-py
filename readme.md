# 💰 Calculadora de Precio de Venta (Colombia)

Una herramienta sencilla y precisa para ayudarte a determinar el precio de venta ideal de tus productos y servicios en Colombia, asegurando que todos los costos e impuestos estén cubiertos y que tu rentabilidad sea la correcta.

---

## ***✨ ¿Qué hace por ti?***

* ### **Pone el IVA (19%)**
  Se encarga de agregar ese impuesto clave sin que tengas que sacar la calculadora.

* ### **Añade la comisión del datáfono**
  Te ayuda a considerar si el cliente te pagará con tarjeta (3% o 3.5% de comisión) para que no pierdas ni un peso de tu ganancia.

* ### **Tiene en cuenta el 4x1000**
  Ese pequeño costo invisible ya está incluido en el cálculo para darte un precio final mucho más realista.

* ### **Es fácil de usar**
  Sólo sigue las instrucciones en pantalla.


## Diagrama de Flujo

graph TD
    A[Inicio] --> B{Solicitar precio base};
    B --> C{Es válido?};
    C -- No --> B;
    C -- Sí --> D[Calcular precio con 19% IVA];
    D --> E{¿Usar datáfono?};
    E -- Sí (3%) --> F[Calcular con 3% de comisión];
    E -- Sí (3.5%) --> G[Calcular con 3.5% de comisión];
    E -- No --> H{¿Agregar 4x1000?};
    F --> H;
    G --> H;
    H -- Sí --> I[Calcular con 0.4% del 4x1000];
    H -- No --> J[Mostrar precio final];
    I --> J;
    J --> K{¿Otra consulta?};
    K -- Sí --> A;
    K -- No --> L[Fin];