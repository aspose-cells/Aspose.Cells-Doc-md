---
title: Aspose.Cells Java pour Jython
type: docs
weight: 70
url: /fr/java/aspose-cells-java-for-jython/
---
## **Introduction**

### **Qu'est-ce que Jython ?**

Jython est une implémentation Java de Python qui combine puissance expressive et clarté. Jython est disponible gratuitement pour une utilisation commerciale et non commerciale et est distribué avec le code source. Jython est complémentaire de Java et convient particulièrement aux tâches suivantes :

- **Scripts intégrés** - Les programmeurs Java peuvent ajouter les bibliothèques Jython à leur système pour permettre aux utilisateurs finaux d'écrire des scripts simples ou compliqués qui ajoutent des fonctionnalités à l'application.
- **Expérimentation interactive** - Jython fournit un interpréteur interactif qui peut être utilisé pour interagir avec les packages Java ou avec les applications Java en cours d'exécution. Cela permet aux programmeurs d'expérimenter et de déboguer n'importe quel système Java en utilisant Jython.
- **Développement rapide d'applications** Les programmes Python sont généralement 2 à 10 fois plus courts que le programme Java équivalent. Cela se traduit directement par une productivité accrue des programmeurs. L'interaction transparente entre Python et Java permet aux développeurs de mélanger librement les deux langages à la fois pendant le développement et lors de la livraison des produits.

### **Aspose.Cells for Java**

Aspose.Cells for Java est une bibliothèque de classe avancée for Java qui vous permet d'effectuer une grande variété de tâches de traitement de documents directement dans votre Java
applications.

Aspose.Cells for Java prend en charge le traitement Cells (DOC, DOCX, OOXML, RTF) HTML, OpenDocument, PDF, EPUB, XPS, SWF et tous les formats d'image. Avec Aspose.Cells vous pouvez
générer, modifier et convertir des documents sans utiliser Microsoft Cells.

### **Aspose.Cells Java pour Jython**

Aspose.Cells Java pour Jython est un projet qui démontre/fournit les exemples d'utilisation Aspose.Cells for Java API dans Jython.

## **Configuration système requise et plates-formes prises en charge**

### **Configuration requise**

**Voici la configuration système requise pour utiliser Aspose.Cells Java pour Jython :**

- Java 1.5 ou supérieur installé
- Composant Aspose.Cells téléchargé
- Jython 2.7.0

### **Plates-formes prises en charge**

**Voici les plates-formes prises en charge :**

- Aspose.Cells 15.4 et supérieur.
- Java EDI (Eclipse, NetBeans...)

## **Télécharger l'installation et l'utilisation**

### **Téléchargement**

**Télécharger des exemples à partir de sites Web de codage social**

Les versions suivantes des exemples d'exécution sont disponibles en téléchargement sur tous les sites de codage social mentionnés ci-dessous :

- [GithubGenericName](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Jython-v1.0.0)

**Télécharger le composant Aspose.Cells for Java**

- [Aspose.Cells for Java](https://releases.aspose.com/cells/java/)

### **Installation**

- Placez le fichier jar Aspose.Cells for Java téléchargé dans le répertoire "lib".
- Remplacez "votre-lib" par le nom du fichier jar téléchargé dans le fichier _*init*_.py.

### **Utilisant**

Vous pouvez créer un document HelloWorld à l'aide de l'exemple de code suivant :

{{< highlight "java" >}}

 from aspose-cells  import Settings

from com.aspose.Cells import Document

from com.aspose.Cells import DocumentBuilder

class HelloWorld:

    def __init__(self):

        dataDir = Settings.dataDir + 'quickstart/'



        workbook = Workbook()



        sheet = workbook.getWorksheets().get(0)



        cell = sheet.getCells().get("A1")



        cell.setValue("Hello World!")



        file_format_type = FileFormatType



        workbook.save(dataDir + "HelloWorld.xls" , file_format_type.EXCEL_97_TO_2003 )



        print "Document has been saved, please check the output file.";

if __name__ == '__main__':

    HelloWorld()

{{< /highlight >}}

## **Soutenir, étendre et contribuer**

### **Soutien**

Dès les premiers jours du Aspose, nous savions que donner à nos clients de bons produits ne suffirait pas. Nous devions également fournir un bon service. Nous sommes nous-mêmes des développeurs et comprenons à quel point il est frustrant lorsqu'un problème technique ou une bizarrerie du logiciel vous empêche de faire ce que vous devez faire. Nous sommes ici pour résoudre les problèmes, pas pour les créer.

C'est pourquoi nous proposons une assistance gratuite. Toute personne qui utilise notre produit, qu'elle l'ait acheté ou utilise une évaluation, mérite toute notre attention et notre respect.

Vous pouvez consigner tous les problèmes ou suggestions liés à Aspose.Cells Java pour Jython à l'aide de l'une des plates-formes suivantes :

- [GithubGenericName](https://github.com/aspose-words/Aspose.Words-for-Java/issues)

### **Prolonger et contribuer**

Aspose.Cells Java pour Jython est open source et son code source est disponible sur les principaux sites Web de codage social répertoriés ci-dessous. Les développeurs sont encouragés à télécharger le code source et à contribuer en suggérant ou en ajoutant de nouvelles fonctionnalités ou en améliorant celles existantes, afin que d'autres puissent également en bénéficier.

### **Code source**

Vous pouvez obtenir le dernier code source à partir de l'un des emplacements suivants

- [GithubGenericName](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Jython-v1.0.0)
