---
title: Compresión HTTP
type: docs
weight: 10
url: /es/net/http-compression/
---

## **Problema de Compresión HTTP**
Algunos usuarios informan que si configuran la Compresión HTTP en IIS, encuentran errores al enviar archivos generados a los navegadores de los clientes.
### **Explicación**
Usamos el encabezado **"Content-disposition", "inline; filename=test.xls"** para forzar al navegador a abrir el archivo y **"Content-disposition", "attachment; filename=test.xls"** para forzar al navegador a abrir el cuadro de diálogo **Guardar como** y usar Microsoft Excel para abrir el archivo. Sin embargo, existen algunas excepciones.
### **Excepciones**
Puedes usar el siguiente código para verificar que NO se trata de un error de Aspose.

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-HTTPCompression.aspx-HTTPCompression.cs" >}}
### **Soluciones**
Puedes usar uno de los siguientes métodos para resolver este problema:

- Mueva esos archivos específicos de ASP.NET (que contienen código que llama a Aspose.Cells) a otra carpeta, que no esté comprimida.
- Desactive la Compresión HTTP para el contenido dinámico.
- Guarde el archivo generado en su servidor y proporcione un enlace a sus usuarios.

Si desea utilizar la Compresión HTTP, por favor siempre utilice la opción *OpenInExcel* en lugar de la opción *OpenInBrowser* cuando sabe que ha habilitado la compresión en IIS.
