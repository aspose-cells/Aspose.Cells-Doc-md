---
title: Licencias
type: docs
weight: 40
url: /es/jasperreports/licensing/
---

{{% alert color="primary" %}}

Aspose.Cells for JasperReports está disponible como una evaluación gratuita e ilimitada en tiempo desde la [página de descargas](https://downloads.aspose.com/cells/jasperreports). La versión de evaluación y las versiones con licencia del producto son la misma descarga.

Cuando esté satisfecho con la versión de evaluación, puede [comprar una licencia](https://purchase.aspose.com/). Asegúrese de comprender y aceptar los términos de la licencia.

La licencia está disponible para descargar desde la página de pedido una vez que el pedido haya sido pagado. La licencia es un archivo XML firmado digitalmente en texto claro. La licencia contiene información como el nombre del cliente, producto adquirido y tipo de licencia. No modifique el contenido del archivo de licencia: hacerlo invalida la licencia.

Hay dos formas de aplicar una licencia:

- [Llame a setLicense](/cells/es/jasperreports/licensing/#call-setlicense)
- [Establezca un parámetro de exportador en applicationContext.xml](/cells/es/jasperreports/licensing/#set-the-licensefile-exporter-parameter-in-applicationcontextxml)

Después de instalar la licencia,

- [Verifique que funciona](/cells/es/jasperreports/licensing/#verify-the-license-works).

{{% /alert %}}

## **Llame a setLicense**

{{% alert color="primary" %}}

Este método es aplicable para usar con JasperReports.

{{% /alert %}}

Descargue la licencia a su computadora y cópiela en la carpeta adecuada (por ejemplo, la carpeta de su aplicación o **JasperReports\lib**).
Agregue el siguiente código a su proyecto:

{{< highlight csharp >}}

import com.aspose.cells.jasperreports.*;

// Create a stream object containing the license file

FileInputStream fstream = new FileInputStream("C:\\Aspose.Cells.JasperReports.lic");

// Set the license through the stream object

License license = new License();

license.setLicense(fstream);

{{< /highlight >}}

## **Establezca el parámetro del archivo de licencia en applicationContext.xml**

{{% alert color="primary" %}}

Este método es aplicable para usar con JasperServer.

{{% /alert %}}

1. Download the license to your computer and copy it to the **\<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF** folder, where **\<InstallDir>** stands for the JasperServer installation directory.
1. Locate the **\<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml** file and add the following lines:

**XML**

{{< highlight csharp >}}

  <bean id="excelACExportParameters" class="com.aspose.cells.jasperreports.ACXlsExportParametersBean">

    <property name="licenseFile" value="C:/jasperserver-3.0/apache-tomcat/webapps/jasperserver/WEB-INF/Aspose.Cells.JasperReports.lic"/>

</bean>

{{< /highlight >}}

## **Verifique que la licencia funcione**

Exporte cualquier informe a formato XLS y verifique si el informe contiene un mensaje de evaluación. Si no hay mensaje de evaluación, entonces la licencia está funcionando correctamente.

**Aspose.Cells for JasperReports inyecta una hoja de cálculo de evaluación en modo de evaluación** 

![todo:image_alt_text](licensing_1.png)

**Cuando hay una licencia válida, no hay hoja de cálculo de evaluación** 

![todo:image_alt_text](licensing_2.png)
