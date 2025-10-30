---
title: Evitar la notación exponencial de números grandes al importar desde HTML con Golang vía C++
linktitle: Evitar la notación exponencial de números grandes al importar desde HTML
type: docs
weight: 10
url: /es/go-cpp/avoid-exponential-notation-of-large-numbers-while-importing-from/
description: Aprenda cómo evitar la notación exponencial para números grandes al importar desde HTML usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

A veces, su HTML contiene números como 1234567890123456 que son más largos que 15 dígitos, y cuando importa su HTML a un archivo de Excel, estos números se convierten en notación exponencial como 1.23457E+15. Si desea que su número se importe tal cual y no se convierta en notación exponencial, utilice la propiedad [**HTMLLoadOptions.GetKeepPrecision()**](https://reference.aspose.com/cells/go-cpp/abstracttextloadoptions/getkeepprecision/) y configúrela en **true** al cargar su HTML.

{{% /alert %}}

El siguiente código de ejemplo explica el uso de la propiedad [**HTMLLoadOptions.GetKeepPrecision()**](https://reference.aspose.com/cells/go-cpp/abstracttextloadoptions/getkeepprecision/). La API importará el número tal cual sin convertirlo en notación exponencial.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AvoidExponentialNotationOfLargeNumbersWhileImportingFromHtml.go" >}}
