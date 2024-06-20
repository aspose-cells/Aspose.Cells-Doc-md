---
title: Evitar la notación exponencial de números grandes al importar desde HTML
type: docs
weight: 10
url: /es/net/avoid-exponential-notation-of-large-numbers-while-importing-from/
---

{{% alert color="primary" %}}

A veces tu Html contiene números como 1234567890123456 que son más largos que 15 dígitos y cuando importas tu HTML a un archivo de excel, estos números se convierten en notación exponencial como 1.23457E+15. Si quieres que tu número se importe tal como es y no se convierta en notación exponencial, entonces por favor usa la propiedad [**HTMLLoadOptions.KeepPrecision**](https://reference.aspose.com/cells/net/aspose.cells/abstracttextloadoptions/properties/keepprecision) y cámbiala a **true** mientras importas tu HTML.

{{% /alert %}}

El siguiente código de muestra explica el uso de la propiedad [**HTMLLoadOptions.KeepPrecision**](https://reference.aspose.com/cells/net/aspose.cells/abstracttextloadoptions/properties/keepprecision). La API importará el número tal como es sin convertirlo en notación exponencial.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AvoidExponentialNotationWhileImportingFromHtml-1.cs" >}}
