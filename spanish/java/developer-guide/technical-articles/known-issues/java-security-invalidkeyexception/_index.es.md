---
title: java.seguridad.InvalidKeyException
type: docs
weight: 10
url: /es/java/java-security-invalidkeyexception/
---
## **Resumen**
De forma predeterminada, AES admite una clave de 128 bits, si planea usar una clave de 192 o 256 bits, el compilador de Java generará una excepción de tamaño de clave ilegal. Esto no se debe a algún error de Aspose.Cells API, sino a la característica limitada de JDK/JRE. Los archivos de política predeterminados de JDK/JRE están paralizados debido a restricciones de importación en algunos países. Los usuarios deben obtener los archivos de política de "Fuerza ilimitada" e instalarlos en su JRE para usar la funcionalidad de criptografía avanzada para el cifrado/descifrado.
## **Síntomas**
 Puede obtener java.security.InvalidKeyException: tamaño de clave ilegal o parámetros predeterminados o java.security.InvalidKeyException: tamaño de clave ilegal al cargar una hoja de cálculo protegida.
## **Solución**
La solución es realmente muy simple como se detalla a continuación.

1. Descargue los archivos de política de jurisdicción de fuerza ilimitada de Java Cryptography Extension (JCE).
1. Extraiga los archivos JAR del archivo descargado y colóquelos en el directorio ${java.home}/jre/lib/security/.
1. Vuelva a ejecutar el programa.
## **Descargar enlaces**
Utilice el enlace de descarga que corresponda a su versión de JDK/JRE.

- [Java Extensión criptográfica (JCE) Archivos de política de jurisdicción de fuerza ilimitada 6](https://www.oracle.com/java/technologies/jce-6-download.html)
- [Java Extensión criptográfica (JCE) Archivos de política de jurisdicción de fuerza ilimitada 7](https://www.oracle.com/java/technologies/jce-7-download.html)
- [Java Extensión criptográfica (JCE) Archivos de política de jurisdicción de fuerza ilimitada 8](https://www.oracle.com/java/technologies/javase-jce8-downloads.html)
