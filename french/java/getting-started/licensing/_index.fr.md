---
title: Licensing
type: docs
weight: 50
url: /fr/java/licensing/
description: Aspose.Cells pour JAVA propose différents plans d'achat ou propose un essai gratuit et une licence temporaire de 30 jours pour évaluation à l'aide du Licensing et des politiques d'abonnement du Java.
keywords: Java Apply License from Disk or Stream. Java Set License from Disk or Stream. Apply License in Aspose.Cells for Java.
---
##  **Comment appliquer une licence dans le composant Aspose.Cells**

La licence est un fichier XML en texte brut qui contient des détails tels que le nom du produit, le nombre de développeurs auxquels il est concédé sous licence, la date d'expiration de l'abonnement, etc. Le fichier est signé numériquement, ne modifiez donc pas le fichier ; même l'ajout par inadvertance d'un saut de ligne supplémentaire dans le fichier l'invalidera.

Vous devez définir une licence avant d'utiliser Aspose.Cells si vous souhaitez éviter ses limitations d'évaluation. Vous n'êtes tenu de définir une licence qu'une seule fois par application ou processus.

La licence peut être chargée à partir d'un flux ou d'un fichier aux emplacements suivants :

1. Chemin explicite.
1. Le dossier qui contient le Aspose.Cells.jar.

 Utilisez le[Licence.setLicense](https://reference.aspose.com/cells/java/com.aspose.cells/license#setLicense(java.io.InputStream)) pour obtenir une licence pour le composant. Souvent, le moyen le plus simple de définir une licence consiste à placer le fichier de licence dans le même dossier que Aspose.Cells.jar et à spécifier uniquement le nom du fichier sans chemin, comme indiqué dans l'exemple suivant :

###  **Comment appliquer une licence à partir du disque**

 Dans cet exemple**Aspose.Cells**tentera de trouver le fichier de licence dans le dossier contenant les JAR de votre application.

{{< highlight "csharp" >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense("Aspose.Cells.Java.lic");

{{< /highlight >}}

###  **Comment appliquer une licence à partir de Stream**

Initialise une licence à partir d'un flux.

{{< highlight "csharp" >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense(new java.io.FileInputStream("Aspose.Cells.Java.lic"));

{{< /highlight >}}

###  **Comment appliquer une licence dans Aspose.Cells.GridWeb**

Il est recommandé de placer le code de licence à un endroit de votre application Web où il doit être traité en premier.

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license file through its path

com.aspose.gridweb.License lic = new com.aspose.gridweb.License();

lic.setLicense("Aspose.Cells.lic");

{{< /highlight >}}

##  **Comment demander une licence limitée**

Aspose.Cells permet aux développeurs d’appliquer une clé mesurée. Il s'agit d'un nouveau mécanisme de licence. Le nouveau mécanisme de licence sera utilisé parallèlement à la méthode de licence existante. Les clients qui souhaitent être facturés en fonction de l'utilisation des fonctionnalités API peuvent utiliser la licence limitée. Pour plus de détails, veuillez vous référer à[FAQ Licensing avec compteur](https://purchase.aspose.com/faqs/licensing/metered)section.

Une nouvelle classe[Compteur](https://reference.aspose.com/cells/java/com.aspose.cells/Metered)été introduit pour appliquer une clé mesurée. Voici un exemple de code montrant comment définir une clé publique et privée mesurée.

{{< highlight "java" >}}

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
