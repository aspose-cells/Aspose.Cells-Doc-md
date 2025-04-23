---
title: java.security.InvalidKeyException
type: docs
weight: 10
url: /es/java/java-security-invalidkeyexception/
---

## **Resumen**
De forma predeterminada, el AES admite una clave de 128 bits, si planea utilizar una clave de 192 bits o 256 bits, el compilador de Java lanzará una excepción de tamaño de clave no válida. Esto no se debe a algún error de la API de Aspose.Cells sino debido a la funcionalidad limitada para JDK/JRE en sí. Los archivos de política predeterminados de JDK/JRE están limitados debido a restricciones de importación en algunos países. Los usuarios tienen que obtener los archivos de política de "Fuerza ilimitada" e instalarlos en su JRE para usar funcionalidades avanzadas de criptografía para cifrado/descifrado.
## **Síntomas**
Puede obtener la java.security.InvalidKeyException: Tamaño de clave no válido o parámetros predeterminados o java.security.InvalidKeyException: Tamaño de clave no válido al cargar una hoja de cálculo protegida. 
## **Solución**
La solución es en realidad muy simple como se detalla a continuación.

1. Descargue la Extensión de Criptografía de Java (JCE) Archivos de Política de Jurisdicción de Fuerza Ilimitada.
1. Extraiga los archivos JAR del archivo descargado y colóquelos en el directorio ${java.home}/jre/lib/security/.
1. Vuelva a ejecutar el programa.
## **Enlaces de Descarga**
Por favor, use el enlace de descarga que corresponda a su versión de JDK/JRE.

- [Java Cryptography Extension (JCE) Archivos de Política de Jurisdicción de Fuerza Ilimitada 6](https://www.oracle.com/java/technologies/jce-6-download.html)
- [Java Cryptography Extension (JCE) Archivos de Política de Jurisdicción de Fuerza Ilimitada 7](https://www.oracle.com/java/technologies/jce-7-download.html)
- [Java Cryptography Extension (JCE) Archivos de Política de Jurisdicción de Fuerza Ilimitada 8](https://www.oracle.com/java/technologies/javase-jce8-downloads.html)
{{< app/cells/assistant language="java" >}}
