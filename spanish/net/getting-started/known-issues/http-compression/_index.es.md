---
title: Compresión HTTP
type: docs
weight: 10
url: /es/net/http-compression/
---
## **Problema de compresión HTTP**
Algunos usuarios informan que si configuran la compresión HTTP en IIS, encuentran errores al enviar archivos generados a los navegadores de los clientes.
### **Explicación**
 Usamos**"Disposición de contenido", "en línea; nombre de archivo = prueba.xls"** encabezado para obligar al navegador a abrir el archivo y**"Disposición de contenido", "archivo adjunto; nombre de archivo = prueba.xls"** encabezado para obligar al navegador a abrir el**Guardar como** y use Microsoft Excel para abrir el archivo. Sin embargo, hay algunas excepciones que existen.
### **Excepciones**
Puede usar el siguiente código para verificar que NO es un error de Aspose.

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-HTTPCompression.aspx-HTTPCompression.cs" >}}
### **Soluciones**
Puede usar una de las siguientes soluciones para resolver este problema:

- Mueva los archivos ASP.NET especificados (que contienen un código que llama a Aspose.Cells) a otra carpeta que no esté comprimida.
- Deshabilite la compresión HTTP para contenido dinámico.
- Guarde el archivo generado en su servidor y proporcione un enlace a sus usuarios.

 Si desea utilizar la compresión HTTP, utilice siempre*AbrirEnExcel* opción en lugar de*Abierta en el navegador* opción cuando sabe que ha habilitado la compresión IIS.
