---
title: Licencia
type: docs
weight: 40
url: /es/jasperreports/licensing/
---
{{% alert color="primary" %}}

 Aspose.Cells for JasperReports está disponible como una evaluación gratuita e ilimitada del[página de descarga](https://downloads.aspose.com/cells/jasperreports). Las versiones de evaluación y con licencia del producto es la misma descarga.

 Cuando esté satisfecho con la versión de evaluación, puede[comprar una licencia](https://purchase.aspose.com/). Asegúrese de comprender y aceptar los términos de la licencia.

La licencia está disponible para su descarga desde la página de pedido cuando el pedido ha sido pagado. La licencia es un archivo XML de texto claro firmado digitalmente. La licencia contiene información como el nombre del cliente, el producto adquirido y el tipo de licencia. No modifique el contenido del archivo de licencia: hacerlo invalida la licencia.

Hay dos formas de solicitar una licencia:

- [Llamar setLicense](/cells/es/jasperreports/licensing/#call-setlicense)
- [Establecer un parámetro de exportador en applicationContext.xml](/cells/es/jasperreports/licensing/#set-the-licensefile-exporter-parameter-in-applicationcontextxml)

Después de instalar la licencia,

- [Verifica que funcione](/cells/es/jasperreports/licensing/#verify-the-license-works).

{{% /alert %}}

## **Llamar setLicense**

{{% alert color="primary" %}}

Este método es aplicable para su uso con JasperReports.

{{% /alert %}}

 Descargue la licencia a su computadora y cópiela en la carpeta adecuada (por ejemplo, la carpeta de su aplicación o**JasperReports\lib**).
Agrega el siguiente código a tu proyecto:

{{< highlight "csharp" >}}

import com.aspose.cells.jasperreports.*;

// Create a stream object containing the license file

FileInputStream fstream = new FileInputStream("C:\\Aspose.Cells.JasperReports.lic");

// Set the license through the stream object

License license = new License();

license.setLicense(fstream);

{{< /highlight >}}

## **Establezca el parámetro del exportador de archivo de licencia en applicationContext.xml**

{{% alert color="primary" %}}

Este método es aplicable para su uso con JasperServer.

{{% /alert %}}

1.  Descargue la licencia a su computadora y cópiela en el**\<dirección de instalación>\apache-tomcat\webapps\jasperserver\WEB-INF**carpeta, donde**\<DirInstalación>** significa el directorio de instalación de JasperServer.
1.  Localiza el**\<dirección de instalación>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml** archivo y agregue las siguientes líneas:

**XML**

{{< highlight "csharp" >}}

  <bean id="excelACExportParameters" class="com.aspose.cells.jasperreports.ACXlsExportParametersBean">

    <property name="licenseFile" value="C:/jasperserver-3.0/apache-tomcat/webapps/jasperserver/WEB-INF/Aspose.Cells.JasperReports.lic"/>

</bean>

{{< /highlight >}}

## **Verificar las obras de la licencia**

Exporte cualquier informe a formato XLS y compruebe si el informe contiene un mensaje de evaluación. Si no hay un mensaje de evaluación, la licencia funciona correctamente.

**Aspose.Cells for JasperReports inyecta una hoja de trabajo de evaluación en modo de evaluación** 

![todo:imagen_alternativa_texto](licensing_1.png)

**Cuando una licencia válida no hay hoja de trabajo de evaluación** 

![todo:imagen_alternativa_texto](licensing_2.png)
