---
title: Problema HTTPS SSL
type: docs
weight: 20
url: /es/net/https-ssl-issue/
---
## **Problema HTTPS/SSL**
Algunos usuarios informaron que tenían problemas para descargar archivos de Excel generados con Aspose.Cells. Cuando se abre el cuadro de diálogo Guardar, el nombre del archivo contiene el nombre de la página aspx en lugar del archivo de Excel, y el Tipo de archivo está en blanco.
### **Explicación**
Cambiamos los encabezados de respuesta HTTP para resolver el problema con la compresión HTTP. Esto puede causar problemas al enviar archivos al navegador del cliente a través de HTTPS/SSL.
### **Solución**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-HTTPSSSLIssue.aspx-SSLIssue.cs" >}}
