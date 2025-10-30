---
title: Evitar la notación exponencial de números grandes al importar desde HTML
type: docs
weight: 10
url: /es/python-net/avoid-exponential-notation-of-large-numbers-while-importing-from/
description: Este tema le muestra cómo evitar la notación exponencial de números grandes al importar desde HTML usando Aspose.Cells para Python via NET.
keywords: Evitar la notación exponencial de números grandes al importar desde HTML, mantener la precisión al importar HTML.
---

{{% alert color="primary" %}}

A veces tu Html contiene números como 1234567890123456 que son más largos que 15 dígitos y cuando importas tu HTML a un archivo de excel, estos números se convierten en notación exponencial como 1.23457E+15. Si quieres que tu número se importe tal como es y no se convierta en notación exponencial, entonces por favor usa la propiedad [**HTMLLoadOptions.keep_precision**](https://reference.aspose.com/cells/python-net/aspose.cells/abstracttextloadoptions/keep_precision/) y cámbiala a **true** mientras importas tu HTML.

{{% /alert %}}

El siguiente código de muestra explica el uso de la propiedad [**HTMLLoadOptions.keep_precision**](https://reference.aspose.com/cells/python-net/aspose.cells/abstracttextloadoptions/keep_precision/). La API importará el número tal como es sin convertirlo en notación exponencial.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-AvoidExponentialNotationWhileImportingFromHtml-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
