---
title: Mise en route de l éditeur de feuilles de calcul
type: docs
weight: 10
url: /fr/java/spreadsheet-editor-getting-started/
---

**Table des matières**

- [Introduction](#SpreadsheetEditorGettingStarted-Introduction)
- [Configuration requise](#SpreadsheetEditorGettingStarted-SystemRequirements)
- [Téléchargement et installation](#SpreadsheetEditorGettingStarted-DownloadandInstallation)
- [Soutien](#SpreadsheetEditorGettingStarted-Support)
- [Contribuer](#SpreadsheetEditorGettingStarted-Contribute)
- [Licence](#SpreadsheetEditorGettingStarted-License)
### **Introduction**
Le Html5 Spreadsheet Editor est une application web qui permet de visualiser et de modifier des documents de feuilles de calcul dans un navigateur web. Il prend en charge les formats Excel, SpreadsheetML, CVS, OpenDocument et de nombreux autres formats supportés par Microsoft Excel. Toutes les fonctionnalités de base, y compris la modification des cellules, la mise en forme, la modification des formules, la gestion des lignes et des colonnes, etc., sont prises en charge.

![todo:image_alt_text](aowcrc1.png)

L'éditeur de feuilles de calcul HTML5 utilise de nombreuses fonctionnalités de [Aspose.Cells for Java](https://products.aspose.com/cells/java/) et montre comment les utiliser pour créer, manipuler et afficher une feuille de calcul dans votre application Java.

**Fonctionnalités**

- Travail avec des fichiers 
  - Formats pris en charge
  - Ouvrir des fichiers locaux
  - Ouvrir depuis Dropbox
  - Ouvrir depuis une URL
  - Créer une nouvelle feuille de calcul
  - Exportation vers divers formats
- Travailler avec des feuilles 
  - Ajouter et supprimer des feuilles
  - Renommer les feuilles
  - Changer de feuilles
- Travailler avec des lignes et des colonnes 
  - Ajouter une ligne
  - Ajouter une colonne
  - Supprimer une ligne
  - Supprimer une colonne
  - Largeur de colonne et hauteur de ligne
- Travailler avec des cellules 
  - Sélectionner une cellule
  - Modifier une cellule
  - Modifier la formule
  - Alignement de la cellule
  - Effacer la cellule
  - Ajouter une cellule
  - Supprimer une cellule
- Travailler avec la mise en forme du texte 
  - Gras, italique, souligné
  - Style et taille de la police
  - Effacer le formatage
### **Configuration requise**
**Configuration logicielle requise**

- Serveur d'application Java CDI pris en charge
- [Aspose.Cells for Java](https://products.aspose.com/cells/java/)
- [JavaServer Faces 2.0](https://javaee.github.io/javaserverfaces-spec/)
- [Primefaces 5.1](https://www.primefaces.org/)

**Configuration matérielle requise**

Les exigences matérielles varient en fonction du serveur d'application Java que nous choisissons pour déployer l'éditeur de feuilles de calcul HTML5 et du nombre de feuilles de calcul que nous ouvrons simultanément. Voici une estimation qui aidera à configurer l'environnement initialement.

- 2 GHz CPU
- 2 GB RAM
- 500 Mo de disque
### **Téléchargement et installation**
L'éditeur de feuilles de calcul HTML5 est une application Java EE et peut être déployé sur n'importe quel serveur d'application Java avec le profil web prenant en charge CDI. Il a été testé avec [Glassfish](https://javaee.github.io/glassfish/).

**Code source**

Le code source du projet est disponible sur [Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/). Nous maintenons également des miroirs Git sur les sites suivants:

- [Bitbucket](https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java)
- [Google Code](https://code.google.com/archive/p/html5-spreadsheet-editor/)
- [SourceForge](https://sourceforge.net/p/html5-spreadsheet-editor/)

Utilisez l'une des commandes suivantes pour télécharger le code source via la ligne de commande:

**Github**

{{< highlight bash >}}

 git clone https://github.com/aspose-cells/Aspose.Cells-for-Java.git

{{< /highlight >}}

**Bitbucket**

{{< highlight bash >}}

 git clone https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java.git

{{< /highlight >}}

**Google Code**

{{< highlight bash >}}

 git clone https://code.google.com/p/html5-spreadsheet-editor/

{{< /highlight >}}

**SourceForge**

{{< highlight bash >}}

 git clone git://git.code.sf.net/p/html5-spreadsheet-editor/code html5-spreadsheet-editor-code

{{< /highlight >}}

**Créer en utilisant Maven**

Le processus de construction du projet est géré en utilisant Maven. Vous pouvez donc préparer un fichier WAR à partir de la ligne de commande sans aucun IDE. Utilisez la commande suivante pour générer un fichier WAR pour le déploiement. La documentation du serveur d'application correspondant vous aidera à déployer le fichier WAR généré et ses dépendances.

{{< highlight java >}}

 mvn clean install

{{< /highlight >}}

**En utilisant NetBeans**

Il est très facile de gérer le projet en utilisant [NetBeans IDE](https://netbeans.apache.org/). NetBeans est l'un des IDE populaires parmi les développeurs Java et est sponsorisé par Oracle.

- Téléchargez le code source du projet.
- Ouvrez le projet dans NetBeans IDE.
- Cliquez sur le bouton ***Exécuter*** dans la barre d'outils.
- Sélectionnez le serveur ***Glassfish*** comme serveur d'application.

**En utilisant Eclipse**

[Eclipse IDE](http://www.eclipse.org/ide/) offre une intégration officielle pour importer des projets Maven appelée [M2Eclipse](http://www.eclipse.org/m2e/):

1. Installez M2Eclipse dans votre Eclipse IDE. La procédure d'installation est décrite sur leur site web.
1. Téléchargez le code source du projet.
1. Ouvrez la boîte de dialogue ***Importer*** dans le menu Fichier.
1. Sélectionnez ***Projet Maven*** dans la boîte de dialogue d'importation.
1. Cliquez sur ***Suivant***.
1. Cliquez sur ***Parcourir*** pour sélectionner l'emplacement du code source.
1. Sélectionnez ***pom.xml*** dans la liste ci-dessous.
1. Cliquez sur ***Terminer***.

L'IDE Eclipse devrait importer et charger le projet.
### **Soutien**
**Rapport de bug**

Pour envoyer un rapport de bug, créez un nouveau problème sur la [page du projet Github](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues) et appliquez l'étiquette ***bug***.

**Demande de fonctionnalité**

Nous apprécions vivement vos commentaires et les fonctionnalités que vous demandez. Pour demander une nouvelle fonctionnalité ou une amélioration existante, veuillez créer un nouveau problème sur la [page du projet Github](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues) et appliquer l'étiquette ***amélioration***.

**Questions et aide**

Vous pouvez poser toutes sortes de questions relatives à l'éditeur de feuilles de calcul HTML5 en utilisant [la section des problèmes Github](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues). Créez simplement un nouveau problème et appliquez l'étiquette ***question***.

**Forums Aspose.Cells for Java**

Les forums des produits Aspose offrent un support complet aux clients d'essai et payants. Les experts sont disponibles 24/7 pour fournir de l'aide et répondre aux questions. Visitez les [forums des produits ici](https://forum.aspose.com/c/cells/9).

**Blogs Aspose**

Restez en contact avec nous et restez informé des dernières nouvelles concernant nos produits et offres. Abonnez-vous à [notre blog ici](http://blog.aspose.com).
### **Contribuer**
[](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java)

[!\[todo:image_alt_text\](https://s3.amazonaws.com/github/ribbons/forkme_right_red_aa0000.png)](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java)


L'éditeur de feuilles de calcul HTML5 est un projet open source qui offre le maximum d'options à tout le monde pour contribuer au projet.

**Code source**

La source du projet est disponible sur [Github](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java). Nous maintenons également des miroirs Git sur les sites suivants:

- [Bitbucket](https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java)
- [SourceForge](https://sourceforge.net/p/html5-spreadsheet-editor/)

**Demandes de tirage**

Pour contribuer au code source du projet, il suffit d'envoyer une demande de tirage via Github. Pour plus d'informations, consultez l'article de Github sur [Créer une demande de tirage](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).
### **Licence**
**Licence MIT**

Nous utilisons l'une des licences open source les plus libérales pour minimiser la responsabilité des contributeurs. HTML5 Spreadsheet Editor est publié sous [Licence MIT](https://opensource.org/licenses/mit-license.php).

**Licence Aspose**

Le produit fonctionne sans licence Aspose, [avec des limitations](/cells/fr/java/licensing/). Pour supprimer les limitations, vous pouvez acquérir une [licence temporaire gratuite](https://purchase.aspose.com/temporary-license) ou [acheter une licence complète](https://purchase.aspose.com/buy).

Par défaut, l'éditeur essaiera de charger le fichier **Aspose.Total.Java.lic** depuis le répertoire **src/main/resources/com/aspose/spreadsheeteditor**. Il suffit de copier le fichier de licence dans ce répertoire. Le comportement par défaut peut être modifié en modifiant la classe **AsposeLicense**.
{{< app/cells/assistant language="java" >}}
