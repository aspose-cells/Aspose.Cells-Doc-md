---
title: Evite la notación exponencial de números grandes al importar desde HTML
type: docs
weight: 600
url: /es/java/avoid-exponential-notation-of-large-numbers-while-importing-from/
---
{{% alert color="primary" %}} 

 veces, su HTML contiene números como 1234567890123456 que tienen más de 15 dígitos y cuando importa su HTML a un archivo de Excel, estos números se convierten en notación exponencial como 1.23457E+15. Si lo desea, su número debe importarse tal como está y no convertirse a notación exponencial, luego use[HtmlLoadOptions.KeepPrecision](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#KeepPrecision) propiedad y establecerlo**verdadero** mientras carga su HTML.

{{% /alert %}} 
## **Evite la notación exponencial de números grandes al importar desde HTML**
 El siguiente código de ejemplo explica el uso de[HtmlLoadOptions.KeepPrecision](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#KeepPrecision)propiedad. Importará el número tal como está sin convertirlo a notación exponencial.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-KeepPrecisionOfLargeNumbers-1.java" >}}
