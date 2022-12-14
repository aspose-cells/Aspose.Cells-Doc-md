---
title: Licence
type: docs
weight: 40
url: /fr/jasperreports/licensing/
---
{{% alert color="primary" %}}

 Aspose.Cells pour JasperReports est disponible sous forme d'évaluation gratuite et illimitée dans le temps auprès du[page de téléchargement](https://downloads.aspose.com/cells/jasperreports). Les versions d'évaluation et sous licence du produit correspondent au même téléchargement.

 Lorsque vous êtes satisfait de la version d'évaluation, vous pouvez[acheter une licence](https://purchase.aspose.com/). Assurez-vous de comprendre et d'accepter les termes de la licence.

La licence est disponible en téléchargement depuis la page de commande une fois la commande payée. La licence est un fichier XML en texte clair signé numériquement. La licence contient des informations telles que le nom du client, le produit acheté et le type de licence. Ne modifiez pas le contenu du fichier de licence : cela invalide la licence.

Il existe deux façons d'appliquer une licence :

- [Appeler setLicense](/cells/fr/jasperreports/licensing/#call-setlicense)
- [Définir un paramètre d'exportateur dans applicationContext.xml](/cells/fr/jasperreports/licensing/#set-the-licensefile-exporter-parameter-in-applicationcontextxml)

Après avoir installé la licence,

- [Vérifiez que cela fonctionne](/cells/fr/jasperreports/licensing/#verify-the-license-works).

{{% /alert %}}

## **Appeler setLicense**

{{% alert color="primary" %}}

Cette méthode est applicable pour une utilisation avec JasperReports.

{{% /alert %}}

Téléchargez la licence sur votre ordinateur et copiez-la dans le dossier approprié (par exemple, le dossier de votre application ou**JasperReports\lib**).
Ajoutez le code suivant à votre projet :

{{< highlight "csharp" >}}

import com.aspose.cells.jasperreports.*;

// Create a stream object containing the license file

FileInputStream fstream = new FileInputStream("C:\\Aspose.Cells.JasperReports.lic");

// Set the license through the stream object

License license = new License();

license.setLicense(fstream);

{{< /highlight >}}

## **Définissez le paramètre licenseFile Exporter dans applicationContext.xml**

{{% alert color="primary" %}}

Cette méthode est applicable pour une utilisation avec JasperServer.

{{% /alert %}}

1.  Téléchargez la licence sur votre ordinateur et copiez-la sur le**\<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF** dossier, où**\<RepInstall>** représente le répertoire d'installation de JasperServer.
1.  Localisez le**\<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml** fichier et ajoutez les lignes suivantes :

**XML**

{{< highlight "csharp" >}}

  <bean id="excelACExportParameters" class="com.aspose.cells.jasperreports.ACXlsExportParametersBean">

    <property name="licenseFile" value="C:/jasperserver-3.0/apache-tomcat/webapps/jasperserver/WEB-INF/Aspose.Cells.JasperReports.lic"/>

</bean>

{{< /highlight >}}

## **Vérifier que la licence fonctionne**

Exportez n'importe quel rapport au format XLS et vérifiez si le rapport contient un message d'évaluation. S'il n'y a pas de message d'évaluation, la licence fonctionne correctement.

**Aspose.Cells pour JasperReports injecte une feuille de calcul d'évaluation en mode d'évaluation** 

![tâche : image_autre_texte](licensing_1.png)

**Lorsqu'une licence valide, il n'y a pas de feuille de travail d'évaluation** 

![tâche : image_autre_texte](licensing_2.png)
