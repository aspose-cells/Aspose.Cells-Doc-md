---
title: Configurando Márgenes
type: docs
weight: 20
url: /es/net/setting-margins/
description: En este artículo, aprenderás cómo establecer los márgenes de una hoja de cálculo de Excel utilizando un código de ejemplo. También aprenderás cómo establecer programáticamente los márgenes para el centro de la página, los márgenes de encabezado y pie de página de Configuración de Página utilizando la API de C# o Biblioteca .NET.
keywords: establecer margen de hoja de cálculo de excel al centro c#, establecer margen de encabezado y pie de página de hoja de cálculo c#
---

{{% alert color="primary" %}}

Aspose.Cells soporta completamente las opciones de configuración de página de Microsoft Excel. Los desarrolladores pueden necesitar configurar ajustes de configuración de página para hojas de cálculo para controlar el proceso de impresión. Este tema discute cómo usar Aspose.Cells para configurar márgenes de página.

{{% /alert %}}

## **Configurando Márgenes**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), que representa un archivo de Excel. La clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene la colección [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet).

La clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) proporciona la propiedad [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) utilizada para establecer las opciones de configuración de página de una hoja de cálculo. El atributo [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) es un objeto de la clase [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) que permite a los desarrolladores establecer diferentes opciones de diseño de página para una hoja de cálculo impresa. La clase [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) proporciona varias propiedades y métodos utilizados para establecer opciones de configuración de página.

### **Márgenes de Página**

Establezca los márgenes de página (izquierdo, derecho, arriba, abajo) utilizando los miembros de la clase [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup). A continuación se enumeran algunos de los métodos que se utilizan para especificar los márgenes de página:

- [**LeftMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/leftmargin)
- [**RightMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/rightmargin)
- [**TopMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/topmargin)
- [**BottomMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/bottommargin)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-1.cs" >}}

### **Centrar en la Página**

Es posible centrar algo en una página horizontal y verticalmente. Para ello, hay algunos miembros útiles de la clase [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup), [**CenterHorizontally**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/centerhorizontally) y [**CenterVertically**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/centervertically).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-CenterOnPage.cs" >}}

### **Márgenes de Encabezado y Pie de Página**

Establezca los márgenes de encabezado y pie de página con los miembros de la clase [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) como [**HeaderMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/headermargin) y [**FooterMargin**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/footermargin).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-HeaderAndFooterMargins.cs" >}}
{{< app/cells/assistant language="csharp" >}}
