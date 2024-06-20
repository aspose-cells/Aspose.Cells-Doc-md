---
title: Licence
type: docs
weight: 40
url: /fr/jasperreports/licensing/
---

{{% alert color="primary" %}}

Aspose.Cells for JasperReports est disponible en téléchargement gratuit et illimité dans le temps depuis la [page de téléchargement](https://downloads.aspose.com/cells/jasperreports). Les versions d'évaluation et sous licence du produit sont les mêmes.

Lorsque vous êtes satisfait de la version d'évaluation, vous pouvez [acheter une licence](https://purchase.aspose.com/). Assurez-vous de comprendre et accepter les termes de la licence.

La licence est disponible en téléchargement à partir de la page de commande une fois la commande payée. La licence est un fichier XML en clair, signé numériquement. La licence contient des informations telles que le nom du client, le produit acheté et le type de licence. Ne modifiez pas le contenu du fichier de licence : cela invalide la licence.

Il existe deux façons d'appliquer une licence :

- [Appelez la méthode setLicense](/cells/fr/jasperreports/licensing/#call-setlicense)
- [Définissez un paramètre d'exportateur dans applicationContext.xml](/cells/fr/jasperreports/licensing/#set-the-licensefile-exporter-parameter-in-applicationcontextxml)

Après avoir installé la licence,

- [Vérifiez si cela fonctionne](/cells/fr/jasperreports/licensing/#verify-the-license-works).

{{% /alert %}}

## **Appelez la méthode setLicense**

{{% alert color="primary" %}}

Cette méthode est applicable pour une utilisation avec JasperReports.

{{% /alert %}}

Téléchargez la licence sur votre ordinateur et copiez-la dans le dossier approprié (par exemple, le dossier de votre application ou **JasperReports\lib**).
Ajoutez le code suivant à votre projet :

{{< highlight csharp >}}

import com.aspose.cells.jasperreports.*;

// Create a stream object containing the license file

FileInputStream fstream = new FileInputStream("C:\\Aspose.Cells.JasperReports.lic");

// Set the license through the stream object

License license = new License();

license.setLicense(fstream);

{{< /highlight >}}

## **Définissez le paramètre d'exportateur licenseFile dans applicationContext.xml**

{{% alert color="primary" %}}

Cette méthode est applicable pour une utilisation avec JasperServer.

{{% /alert %}}

1. Download the license to your computer and copy it to the **\<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF** folder, where **\<InstallDir>** stands for the JasperServer installation directory.
1. Locate the **\<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml** file and add the following lines:

**XML**

{{< highlight csharp >}}

  <bean id="excelACExportParameters" class="com.aspose.cells.jasperreports.ACXlsExportParametersBean">

    <property name="licenseFile" value="C:/jasperserver-3.0/apache-tomcat/webapps/jasperserver/WEB-INF/Aspose.Cells.JasperReports.lic"/>

</bean>

{{< /highlight >}}

## **Vérifier si la licence fonctionne**

Exportez n'importe quel rapport au format XLS et vérifiez si le rapport contient un message d'évaluation. S'il n'y a aucun message d'évaluation, alors la licence fonctionne correctement.

**Aspose.Cells for JasperReports injecte une feuille de calcul d'évaluation en mode d'évaluation** 

![todo:image_alt_text](licensing_1.png)

**Lorsqu'une licence valide est présente, il n'y a pas de feuille de calcul d'évaluation** 

![todo:image_alt_text](licensing_2.png)
