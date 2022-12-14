---
title: Evite la notación exponencial de números grandes al importar desde HTML
type: docs
weight: 10
url: /es/net/avoid-exponential-notation-of-large-numbers-while-importing-from/
---
{{% alert color="primary" %}}

 A veces, su Html contiene números como 1234567890123456 que tienen más de 15 dígitos y cuando importa su HTML a un archivo de Excel, estos números se convierten en notación exponencial como 1.23457E+15. Si lo desea, su número debe importarse tal como está y no convertirse a notación exponencial, luego use[**HTMLLoadOptions.KeepPrecision**](https://reference.aspose.com/cells/net/aspose.cells/abstracttextloadoptions/properties/keepprecision) propiedad y establecerlo**verdadero** mientras carga su HTML.

{{% /alert %}}

 El siguiente código de ejemplo explica el uso de[**HTMLLoadOptions.KeepPrecision**](https://reference.aspose.com/cells/net/aspose.cells/abstracttextloadoptions/properties/keepprecision)propiedad. El API importará el número tal cual sin convertirlo a notación exponencial.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AvoidExponentialNotationWhileImportingFromHtml-1.cs" >}}
