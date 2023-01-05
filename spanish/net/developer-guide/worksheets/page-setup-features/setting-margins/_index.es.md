---
title: Configuración de márgenes
type: docs
weight: 20
url: /es/net/setting-margins/
---
{{% alert color="primary" %}}

Aspose.Cells es totalmente compatible con las opciones de configuración de página de Microsoft de Excel. Es posible que los desarrolladores necesiten configurar los ajustes de configuración de la página para que las hojas de trabajo controlen el proceso de impresión. Este tema trata sobre cómo usar Aspose.Cells para configurar los márgenes de página.

{{% /alert %}}

## **Configuración de márgenes**

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , que representa un archivo de Excel. Él[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) clase contiene el[**Hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) colección que permite el acceso a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)clase.

 Él[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la clase proporciona la[**Configuración de página**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) propiedad utilizada para establecer las opciones de configuración de página para una hoja de trabajo. Él[**Configuración de página**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) atributo es un objeto de la[**Configuración de página**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) clase que permite a los desarrolladores establecer diferentes opciones de diseño de página para una hoja de trabajo impresa. Él[**Configuración de página**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)La clase proporciona varias propiedades y métodos que se utilizan para establecer las opciones de configuración de la página.

### **Márgenes de página**

 Configure los márgenes de la página (izquierda, derecha, arriba, abajo) usando[**Configuración de página**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup)miembros de la clase A continuación se enumeran algunos de los métodos que se utilizan para especificar los márgenes de página:

- [**Margen izquierdo**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/leftmargin)
- [**Margen derecho**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/rightmargin)
- [**Margen superior**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/topmargin)
- [**Margen inferior**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/bottommargin)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-1.cs" >}}

### **Centrar en la página**

Es posible centrar algo en una página horizontal y verticalmente. Para esto, hay algunos miembros útiles de la[**Configuración de página**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) clase,[**CentroHorizontalmente**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/centerhorizontally) y[**CentroVerticalmente**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/centervertically).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-CenterOnPage.cs" >}}

### **Márgenes de encabezado y pie de página**

 Establecer márgenes de encabezado y pie de página con el[**Configuración de página**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/pagesetup) miembros de la clase como[**Margen de encabezado**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/headermargin) y[**Margen de pie de página**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/footermargin).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetMargins-HeaderAndFooterMargins.cs" >}}
