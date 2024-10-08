# Análisis de Algoritmos: Suffix Array, Burrows-Wheeler Transform y Arreglos C y Occur

Durante esta actividad se tuvo una conversación con ChatGPT en la cual se implementaron algunos algoritmos, analizando la información compartida en comparación con las diapositivas dadas en clase y con una investigación adicional sobre estos algoritmos.

![image](https://github.com/user-attachments/assets/13bb485d-1ba5-4483-8694-30ececf16ab5)

## 1. Suffix Array

### Nuestra Información
El Suffix Array es una estructura de datos que contiene los índices de los sufijos de una cadena ordenados lexicográficamente. Los algoritmos más eficientes para construir un Suffix Array pueden lograr una complejidad de O(n) utilizando técnicas como el algoritmo de Kärkkäinen-Sanders. Además, el Suffix Array es fundamental para diversas aplicaciones, incluyendo búsqueda de patrones y compresión de datos.

![image](https://github.com/user-attachments/assets/8d427dac-252d-4e52-816f-2b343c0de0c1)


### Lo que Dice la Conversación
En la conversación, se discutió un método básico para construir el Suffix Array al generar todos los sufijos y ordenarlos, lo que implica una complejidad temporal de O(n² log n). Sin embargo, no se mencionó la existencia de algoritmos más eficientes que podrían reducir significativamente esta complejidad. La conversación se centró en una implementación sencilla sin discutir los métodos avanzados que se pueden aplicar.

![image](https://github.com/user-attachments/assets/c11c3112-6b43-4131-931b-fd462935bc6b)

### Cuestionamientos y Errores
- **Falta de menciones a algoritmos eficientes:** No se mencionó el algoritmo de Kärkkäinen-Sanders ni otros métodos que permiten construir el Suffix Array en O(n) tiempo, lo cual es crítico para aplicaciones con grandes volúmenes de datos.
  
- **Complejidad espacial no discutida:** Aunque se menciona la complejidad temporal, la complejidad espacial, que puede ser O(n²) en el peor de los casos debido al almacenamiento de sufijos, no se trata en la conversación. Esto puede ser problemático en aplicaciones donde la memoria es una consideración importante.

## 2. Burrows-Wheeler Transform (BWT)

### Nuestra Información
La BWT es una transformación que reorganiza el texto para que caracteres similares queden juntos, mejorando la compresión. Se construye a partir del Suffix Array, y su complejidad de construcción es O(n). La BWT se utiliza en combinación con el FM-Index para realizar búsquedas eficientes.

![image](https://github.com/user-attachments/assets/b3ed14d1-4bde-434e-b014-b760b05462ab)

### Lo que Dice la Conversación
La conversación describe correctamente la BWT como una permutación del texto basada en el Suffix Array, con una complejidad temporal de O(n). Sin embargo, no se menciona en detalle el propósito de la BWT y cómo mejora la compresión y la búsqueda de patrones.

![image](https://github.com/user-attachments/assets/1a4f4e59-dba6-4c33-8b17-4da4799a1a60)

![image](https://github.com/user-attachments/assets/c372d18e-92d8-4d9c-849c-8addc5d0878e)

### Cuestionamientos y Errores
- **Propósito de la BWT no discutido:** Aunque se menciona que la BWT agrupa caracteres, no se detalla cómo esto mejora la compresión. La conversación podría beneficiarse de una discusión sobre el impacto de la BWT en la eficiencia de algoritmos de búsqueda.

- **Falta de alternativas para la construcción:** No se mencionan métodos alternativos o eficientes para construir la BWT, lo que podría haber enriquecido el entendimiento de la implementación.

  ![image](https://github.com/user-attachments/assets/01458821-4461-4899-a3b4-b6b2c7b71330)


## 3. Arreglos C y Occur

### Nuestra Información
Los arreglos C y Occur son fundamentales para el FM-Index. El arreglo C proporciona un conteo de cuántos caracteres lexicográficamente menores aparecen en el texto, mientras que Occur mantiene un conteo acumulado de las ocurrencias de cada carácter en la BWT.

![image](https://github.com/user-attachments/assets/860123b8-67d4-48bd-a758-f0f9a5c8eb6a)

### Lo que Dice la Conversación
La conversación describe cómo construir los arreglos C y Occur, enfatizando su utilidad en el FM-Index. Se menciona la complejidad temporal de O(n) para la construcción de C y O(n ⋅ |Σ|) para Occur. Sin embargo, no se aborda la complejidad espacial de estos arreglos ni se discuten optimizaciones posibles.

## 4. FM-Index

### Nuestra información:
El FM-Index es una estructura de datos que permite la búsqueda eficiente de patrones en textos comprimidos, utilizando la Burrows-Wheeler Transform (BWT) y los arreglos C y Occur. El FM-Index aprovecha la propiedad de la BWT de agrupar caracteres similares, lo que facilita la búsqueda en O(m) tiempo, donde m es la longitud del patrón. Esta eficiencia se logra mediante una búsqueda en reversa (backward search), que recorre el patrón de derecha a izquierda.

![image](https://github.com/user-attachments/assets/551bc5b7-21fb-404b-bfdd-a903acaa0b1f)


### Lo que dice la conversación:
En la conversación, se discute la construcción del FM-Index y la función backwardSearch, que utiliza la BWT, C y Occur para realizar búsquedas de patrones. Se menciona que la complejidad temporal para la búsqueda es O(m), y que esta metodología es eficiente. Sin embargo, no se mencionan detalles sobre cómo se implementa el FM-Index en su totalidad, ni se discuten las optimizaciones que se pueden aplicar para mejorar su rendimiento.

![image](https://github.com/user-attachments/assets/6644f983-71f3-4b6a-8d0c-7bf56e74655c)

![image](https://github.com/user-attachments/assets/97b4024e-9728-48d4-98c8-0679ff9654ba)


## Cuestionamientos y errores:

- **Falta de detalles sobre la construcción del FM-Index:** Aunque se menciona la búsqueda usando el FM-Index, no se discute cómo se construye esta estructura de manera completa. Wikipedia proporciona una descripción más exhaustiva de cómo se combinan la BWT y los arreglos C y Occur para formar el FM-Index, lo que sería valioso para una comprensión más profunda.

- **Omisión de optimizaciones:** La conversación no considera optimizaciones potenciales para el FM-Index, como el uso de compresión en los arreglos C y Occur, que podría reducir el uso de memoria y mejorar el rendimiento general. Wikipedia menciona que el uso de técnicas de compresión puede ser ventajoso en textos largos.

### Cuestionamientos y Errores
- **Complejidad espacial no discutida:** Aunque se menciona que el arreglo Occur tiene una complejidad de O(n ⋅ |Σ|), no se discute la necesidad de este almacenamiento, lo que puede ser problemático para textos grandes.

- **Falta de optimizaciones:** No se mencionan técnicas de optimización, como el uso de Run-Length Encoding (RLE), que podrían ayudar a reducir el uso de memoria en el arreglo Occur. La omisión de estas optimizaciones limita la discusión sobre la eficiencia de la implementación.

## Conclusiones Generales

La conversación ofrece un entendimiento básico sobre el Suffix Array, la BWT, y los arreglos C y Occur, pero carece de detalles críticos que podrían enriquecer la comprensión y mejorar la implementación. Las siguientes conclusiones se pueden extraer:

1. **Falta de mención de algoritmos eficientes:** La conversación no aborda algoritmos avanzados que podrían mejorar significativamente el rendimiento de la implementación.

2. **Omisiones en la discusión de complejidades:** La complejidad espacial de las estructuras no se analiza adecuadamente, lo que puede tener un impacto significativo en aplicaciones prácticas.

3. **No se considera la compresión:** La falta de discusión sobre técnicas como RLE limita las oportunidades para optimizar el uso de memoria, lo que es esencial para aplicaciones de gran escala.

4. **Poco enfoque en aplicaciones prácticas:** Aunque se menciona la importancia de estas estructuras en la búsqueda y compresión de datos, la conversación no profundiza en cómo se aplican en contextos reales.

Este análisis crítico pone de relieve las deficiencias en la conversación y la importancia de profundizar en los detalles y técnicas avanzadas cuando se trata de implementar algoritmos de búsqueda y compresión en textos.

Para ver la conversación continua, se puede ver en el siguiente enlace: https://chatgpt.com/share/67048d18-dd4c-8003-a2ab-4d3e08f7b608 

![image](https://github.com/user-attachments/assets/cfed3dee-c585-4b20-8c17-a2f890b946c3)

## Conclusiones Individuales

### Alejandro Kong:

Esta actividad me permitió explorar conceptos avanzados de búsqueda de subcadenas, como el Suffix Array, la Burrows-Wheeler Transform (BWT) y el FM-Index. Colaborar en equipo y utilizar Git fue esencial para organizar nuestro trabajo y documentar el proceso.
En este caso me toco implementar el Suffix Array, con la ayuda de ChatGPT, facilitó mi comprensión de cómo estas estructuras optimizan la búsqueda en cadenas largas. También aprendí a analizar la complejidad temporal y espacial de nuestros algoritmos, lo que es crucial para mejorar su eficiencia. Esta experiencia me ayudó a reforzar mis conocimientos en estructuras de datos y a apreciar el valor de los grandes modelos de lenguaje en la programación.

### Miranda Arróniz:

En la actividad de búsqueda en cadenas como el FM-Index, Burrows-Wheeler Transform (BWT) y Suffix Arrays, me enfoqué en implementar el BWT con la ayuda de ChatGPT-4. Contar con la ayuda de ChatGPT fue útil para entender cómo estas estructuras optimizan la búsqueda de datos. También comparé en tiempo y espacio la eficiencia del BWT con los algoritmos que mis demás compañeros implementamos. También use Git para coordinar y documentar el proyecto. Al final, esta experiencia me demostró lo útil que es la IA en programación y aprendizaje.

### Estefanía Antonio:

Este proyecto me permitió profundizar en algoritmos avanzados y aplicar estructuras de datos complejas de manera práctica. El uso de Chat GPT fue enriquecedor, ya que facilitó la iteración rápida y la resolución eficiente de problemas. Sin embargo, es esencial complementar esta tecnología con un sólido conocimiento teórico para garantizar la precisión de las soluciones. El análisis de una cadena de genoma y la búsqueda de la subcadena “TCGA” demostraron la versatilidad de estos algoritmos en bioinformática, ampliando mi perspectiva sobre sus aplicaciones reales en la ciencia. La actividad fue un desafío que me permitió aplicar conocimientos y explorar nuevas tecnologías. Estoy satisfecha con el resultado y motivada a seguir investigando el potencial de la inteligencia artificial en la biología y la salud. Además, aprendí que formular preguntas de una manera descriptiva, amplia y amable es vital para obtener respuestas más detalladas y útiles de ChatGPT. Pedir de manera clara y estructurada no solo mejora la calidad de las respuestas, sino que también facilita un proceso más eficiente y fructífero en la resolución de problemas complejos.
