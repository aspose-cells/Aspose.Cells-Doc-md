---
title: Licence
type: docs
weight: 50
url: /fr/java/licensing/
---
{{% alert color="primary" %}} 

 Vous pouvez télécharger une version d'évaluation de**Aspose.Cells** for Java de[sa page de téléchargement](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-cells) @ Maven repos. La version d'évaluation fournit absolument les mêmes fonctionnalités que la version sous licence du produit. De plus, la version d'évaluation devient simplement sous licence lorsque vous achetez une licence et ajoutez quelques lignes de code pour appliquer la licence.

 Une fois que vous êtes satisfait de votre évaluation de**Aspose.Cells** , tu peux[acheter une licence](https://purchase.aspose.com)sur le site Aspose. Familiarisez-vous avec les différents types d'abonnements proposés. Si vous avez des questions, n'hésitez pas à contacter l'équipe commerciale au Aspose.

Chaque licence Aspose comporte un abonnement d'un an pour des mises à niveau gratuites vers toutes les nouvelles versions ou correctifs qui sortent pendant cette période. Le support technique est gratuit et illimité et fourni à la fois aux utilisateurs sous licence et aux utilisateurs d'évaluation.

{{% /alert %}} {{% alert color="primary" %}} 

 Si vous voulez tester**Aspose.Cells** sans limitation de version d'évaluation, demandez une licence temporaire de 30 jours. Prière de se référer à[Comment obtenir une licence temporaire ?](https://purchase.aspose.com/temporary-license) pour plus d'informations.

{{% /alert %}}

## **Limites de la version d'évaluation**

 Version d'évaluation de**Aspose.Cells** produit (sans licence spécifiée) fournit toutes les fonctionnalités du produit, mais il est limité à l'ouverture de 100 fichiers dans un programme et d'une feuille de calcul supplémentaire avec filigrane d'évaluation.

Les limites sont indiquées ci-dessous :

### **1ère limitation : nombre de fichiers ouverts**

Lors de l'exécution de votre programme, vous ne pouvez ouvrir que 100 fichiers Excel. Si votre application dépasse ce nombre, une exception sera levée.

### **2e limitation : feuille de calcul avec filigrane d'évaluation**

![tâche : image_autre_texte](licensing_1.png)

Cette feuille de calcul s'affichera toujours comme feuille de calcul active. Uniquement dans la version sous licence, vous pouvez définir la feuille de calcul active sur d'autres feuilles de calcul.

## **Définition d'une licence**

La licence est un fichier XML en texte brut qui contient des détails tels que le nom du produit, le nombre de développeurs auxquels il est licencié, la date d'expiration de l'abonnement, etc. Le fichier est signé numériquement, ne modifiez donc pas le fichier ; même l'ajout par inadvertance d'un saut de ligne supplémentaire dans le fichier l'invalidera.

Vous devez définir une licence avant d'utiliser Aspose.Cells si vous souhaitez éviter ses limites d'évaluation. Vous n'êtes tenu de définir une licence qu'une seule fois par application ou processus.

La licence peut être chargée à partir d'un flux ou d'un fichier aux emplacements suivants :

1. Chemin explicite.
1. Le dossier qui contient le fichier Aspose.Cells.jar.

 Utilisez le[License.setLicense](https://reference.aspose.com/cells/java/com.aspose.cells/license#setLicense(java.io.InputStream)) pour obtenir la licence du composant. Souvent, le moyen le plus simple de définir une licence consiste à placer le fichier de licence dans le même dossier que Aspose.Cells.jar et à spécifier uniquement le nom du fichier sans chemin, comme indiqué dans l'exemple suivant :

### **Exemple 1**

 Dans cet exemple**Aspose.Cells** tentera de trouver le fichier de licence dans le dossier contenant les fichiers JAR de votre application.

{{< highlight "csharp" >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense("Aspose.Cells.Java.lic");

{{< /highlight >}}

### **Exemple 2**

Initialise une licence à partir d'un flux.

{{< highlight "csharp" >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense(new java.io.FileInputStream("Aspose.Cells.Java.lic"));

{{< /highlight >}}

### **Remarques sur l'application d'une licence dans Aspose.Cells.GridWeb**

Il est recommandé de placer le code de licence à un endroit de votre application Web où il doit être traité en premier.

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license file through its path

com.aspose.gridweb.License lic = new com.aspose.gridweb.License();

lic.setLicense("Aspose.Cells.lic");

{{< /highlight >}}

## **Application d'une licence limitée**

Aspose.Cells permet aux développeurs d'appliquer une clé mesurée. Il s'agit d'un nouveau mécanisme d'octroi de licences. Le nouveau mécanisme d'octroi de licences sera utilisé parallèlement à la méthode d'octroi de licences existante. Les clients qui souhaitent être facturés en fonction de l'utilisation des fonctionnalités API peuvent utiliser la licence mesurée. Pour plus de détails, veuillez consulter[FAQ sur les licences limitées](https://purchase.aspose.com/faqs/licensing/metered)section.

Une nouvelle classe[Compteur](https://reference.aspose.com/cells/java/com.aspose.cells/Metered)a été introduit pour appliquer la clé mesurée. Voici l'exemple de code montrant comment définir une clé publique et privée mesurée.

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
