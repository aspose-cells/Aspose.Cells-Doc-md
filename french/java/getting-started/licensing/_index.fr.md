---
title: Licence
type: docs
weight: 50
url: /fr/java/licensing/
description: Aspose.Cells for JAVA propose différents plans d achat ou offre un essai gratuit et une licence temporaire de 30 jours pour l évaluation en utilisant la politique de licences et d abonnement en Java.
keywords: Java Appliquer la licence depuis le disque ou le flux. Java Définir une licence depuis le disque ou le flux. Appliquer la licence en Aspose.Cells for Java.
---

## **Comment appliquer une licence dans le composant Aspose.Cells**

La licence est un fichier XML en texte clair qui contient des détails tels que le nom du produit, le nombre de développeurs pour lequel il est autorisé, la date d'expiration de l'abonnement, etc. Le fichier est signé numériquement, donc ne le modifiez pas; même l'ajout involontaire d'un saut de ligne supplémentaire le rendra invalide.

Vous devez définir une licence avant d'utiliser Aspose.Cells si vous voulez éviter ses limitations d'évaluation. Vous devez définir une licence une seule fois par application ou processus.

La licence peut être chargée à partir d'un flux ou d'un fichier dans les emplacements suivants :

1. Chemin explicite.
1. Le dossier contenant Aspose.Cells.jar.

Utilisez la méthode [License.setLicense](https://reference.aspose.com/cells/java/com.aspose.cells/license#setLicense-java.io.InputStream-) pour licencier le composant. La manière la plus simple de définir une licence est de placer le fichier de licence dans le même dossier que Aspose.Cells.jar et de spécifier uniquement le nom du fichier sans le chemin, comme dans l'exemple suivant :

### **Comment appliquer une licence depuis le disque**

Dans cet exemple, **Aspose.Cells** tentera de trouver le fichier de licence dans le dossier contenant les JAR de votre application.

{{< highlight csharp >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense("Aspose.Cells.Java.lic");

{{< /highlight >}}

### **Comment appliquer une licence depuis un flux**

Initialise une licence à partir d'un flux.

{{< highlight csharp >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense(new java.io.FileInputStream("Aspose.Cells.Java.lic"));

{{< /highlight >}}

### **Comment appliquer une licence dans Aspose.Cells.GridWeb**

Il est recommandé de placer le code de licence à un endroit dans votre application web où il devrait être traité en premier.

{{< highlight csharp >}}

//Instantiate an instance of license and set the license file through its path

com.aspose.gridweb.License lic = new com.aspose.gridweb.License();

lic.setLicense("Aspose.Cells.lic");

{{< /highlight >}}

## **Comment appliquer une licence mesurée**

Aspose.Cells permet aux développeurs d'appliquer une clé mesurée. Il s'agit d'un nouveau mécanisme de licence. Le nouveau mécanisme de licence sera utilisé avec la méthode de licence existante. Les clients qui veulent être facturés en fonction de l'utilisation des fonctionnalités de l'API peuvent utiliser la licence mesurée. Pour plus de détails, veuillez vous référer à la section [FAQ sur la Licence Mesurée](https://purchase.aspose.com/faqs/licensing/metered).

Une nouvelle classe [Mesuré](https://reference.aspose.com/cells/java/com.aspose.cells/Metered) a été introduite pour appliquer la clé mesurée. Voici un exemple de code démontrant comment définir une clé publique et privée mesurée.

{{< highlight java >}}

//Set metered public and private keys

Metered metered = new Metered();

//Access the setMeteredKey property and pass public and private keys as parameters

metered.setMeteredKey("************", "************");

//Instantiate a new Workbook

Workbook workbook = new Workbook();

//Check if the license is set

System.out.println(workbook.isLicensed());

//Get the Consumption quantity

double amountBefore = Metered.getConsumptionQuantity();

System.out.println(amountBefore);

Workbook workbook2 = new Workbook("Book1.xlsx");

workbook2.save("out1.xlsx");

//Get the Consumption quantity again which should be greater a bit

double amountAfter = Metered.getConsumptionQuantity();

System.out.println(amountAfter);

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
