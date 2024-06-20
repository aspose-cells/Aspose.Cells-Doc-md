---
title: Evitar la notación exponencial de números grandes al importar desde HTML
type: docs
weight: 600
url: /es/java/avoid-exponential-notation-of-large-numbers-while-importing-from/
---

{{% alert color="primary" %}} 

A veces su HTML contiene números como 1234567890123456 que son más largos de 15 dígitos y cuando importa su HTML a un archivo de Excel, estos números se convierten a notación exponencial como 1.23457E+15. Si desea que su número se importe tal como está y no se convierta a notación exponencial, then use [HtmlLoadOptions.KeepPrecision](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#KeepPrecision) propiedad y establezca **true** mientras carga su HTML.

{{% /alert %}} 
## **Evitar la notación exponencial de números grandes al importar desde HTML**
El siguiente código de muestra explica el uso de la propiedad [HtmlLoadOptions.KeepPrecision](https://reference.aspose.com/cells/java/com.aspose.cells/htmlloadoptions#KeepPrecision). Importará el número tal como está sin convertirlo a notación exponencial.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-KeepPrecisionOfLargeNumbers-1.java" >}}
