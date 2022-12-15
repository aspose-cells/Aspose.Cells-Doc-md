---
title: Éditeur de feuille de calcul
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
Html5 Spreadsheet Editor est une application Web qui peut afficher et modifier des feuilles de calcul dans un navigateur Web. Il prend en charge Excel, SpreadsheetML, CVS, OpenDocument et de nombreux autres formats pris en charge par Microsoft Excel. Toutes les fonctionnalités de base, y compris l'édition de cellules, le formatage, l'édition de formules, la gestion des lignes et des colonnes, etc. sont prises en charge.

![tâche : image_autre_texte](aowcrc1.png)

 HTML5 Spreadsheet Editor utilise de nombreuses fonctionnalités de[Aspose.Cells for Java](https://products.aspose.com/cells/java/)et montre comment les utiliser pour créer, manipuler et afficher une feuille de calcul dans votre application Java.

**Fonctionnalités**

-  Travailler avec des fichiers
 - Formats pris en charge
 - Ouvrir les fichiers locaux
 - Ouvrir depuis Dropbox
 - Ouvrir à partir de l'URL
 - Créer une nouvelle feuille de calcul
 - Exporter vers différents formats
-  Travailler avec des feuilles
 - Ajouter et supprimer des feuilles
 - Renommer les feuilles
 - Basculer entre les feuilles
-  Travailler avec des lignes et des colonnes
 - Ajouter une ligne
 - Ajouter une colonne
 - Supprimer une ligne
 - Supprimer une colonne
 - Largeur de colonne et hauteur de ligne
-  Travailler avec Cells
 - Sélection d'une cellule
 - Modification d'une cellule
 - Formule d'édition
 - alignement Cell
 - Clair Cell
 - Ajouter une cellule
 - Supprimer une cellule
-  Travailler avec la mise en forme du texte
 - Gras, italique, souligné
 - Style et taille de la police
 - Supprimer le formattage
### **Configuration requise**
**Logiciels requis**

- Serveur d'applications Java pris en charge par CDI
- [Aspose.Cells for Java](https://products.aspose.com/cells/java/)
- [JavaServer Faces 2.0](https://javaee.github.io/javaserverfaces-spec/)
- [Primefaces 5.1](https://www.primefaces.org/)

**Exigences matérielles**

La configuration matérielle requise varie en fonction du serveur d'applications Java que nous choisissons pour déployer HTML5 Spreadsheet Editor et du nombre de feuilles de calcul que nous ouvrons simultanément. Voici une estimation, qui vous aidera à configurer initialement l'environnement.

- Processeur 2 GHz
- 2 Go de RAM
- Disque de 500 Mo
### **Téléchargement et installation**
 HTML5 Spreadsheet Editor est une application Java EE et peut être déployée sur n'importe quel profil Web de serveur d'applications Java avec prise en charge CDI. Il a été testé avec[Poisson de verre](https://javaee.github.io/glassfish/).

**Code source**

 La source du projet est disponible sur[GithubGenericName](https://github.com/aspose-cells/Aspose.Cells-for-Java/). Nous maintenons également des miroirs Git sur les sites suivants :

- [Bitbucket](https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java)
- [Code Google](https://code.google.com/archive/p/html5-spreadsheet-editor/)
- [SourceForge](https://sourceforge.net/p/html5-spreadsheet-editor/)

Utilisez l'une des commandes suivantes pour télécharger le code source via la ligne de commande :

**GithubGenericName**

{{< highlight "bash" >}}

 git clone https://github.com/aspose-cells/Aspose.Cells-for-Java.git

{{< /highlight >}}

**Bitbucket**

{{< highlight "bash" >}}

 git clone https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java.git

{{< /highlight >}}

**Code Google**

{{< highlight "bash" >}}

 git clone https://code.google.com/p/html5-spreadsheet-editor/

{{< /highlight >}}

**SourceForge**

{{< highlight "bash" >}}

 git clone git://git.code.sf.net/p/html5-spreadsheet-editor/code html5-spreadsheet-editor-code

{{< /highlight >}}

**Construire en utilisant Maven**

Le processus de construction du projet est géré à l'aide de Maven. Vous pouvez donc préparer un fichier WAR à partir de la ligne de commande sans aucun IDE. Utilisez la commande suivante pour générer un fichier WAR pour le déploiement. La documentation du serveur d'application correspondant vous aidera à déployer le WAR généré et ses dépendances.

{{< highlight "java" >}}

 mvn clean install

{{< /highlight >}}

**Utilisation de NetBeans**

 Il est très facile de gérer le projet en utilisant[EDI NetBeans](https://netbeans.apache.org/). NetBeans est l'un des IDE populaires parmi les développeurs Java et est sponsorisé par Oracle.

- Téléchargez le code source du projet.
- Ouvrez le projet dans NetBeans IDE.
-  Cliquez sur***Courir*** bouton de la barre d'outils.
-  Sélectionner***Poisson de verre*** serveur en tant que serveur d'applications.

**Utiliser Éclipse**

[Eclipse EDI](http://www.eclipse.org/ide/) fournit une intégration officielle pour importer des projets Maven appelés[M2Éclipse](http://www.eclipse.org/m2e/):

1. Installez M2Eclipse dans votre IDE Eclipse. La procédure d'installation est décrite sur leur site internet.
1. Téléchargez le code source du projet.
1. Ouvrez le***Importer*** boîte de dialogue du menu Fichier.
1.  Sélectionner***Maven Projet*** depuis la boîte de dialogue d'importation.
1.  Cliquez sur***Prochain***.
1.  Cliquez sur***Parcourir*** pour sélectionner l'emplacement du code source.
1.  Sélectionner***pom.xml*** de la liste ci-dessous.
1.  Cliquez sur***Finir***.

L'IDE Eclipse doit importer et charger le projet.
### **Soutien**
**Rapport d'erreur**

 Pour envoyer un rapport de bogue, créez un nouveau problème à[Page du projet Github](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues) et appliquer l'étiquette***punaise***.

**Demande de fonctionnalité**

 Nous apprécions grandement vos commentaires et les fonctionnalités que vous demandez. Pour demander une nouvelle fonctionnalité ou une amélioration dans une version existante, veuillez créer un nouveau problème à[Page du projet Github](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues) et appliquer l'étiquette***renforcement***.

**Questions et aide**

 Vous pouvez poser toutes sortes de questions liées à HTML5 Spreadsheet Editor en utilisant[Problème Github](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java/issues) . Créez simplement un nouveau problème et appliquez le***question*** étiquette.

**Aspose.Cells for Java Forums**

 Les forums de produits Aspose offrent une assistance complète pour les clients d'essai et payants. Des experts sont présents 24h/24 et 7j/7 pour fournir de l'aide et répondre aux questions. Visite[forums de produits ici](https://forum.aspose.com/c/cells/9).

**Aspose Blogues**

 Contactez-nous et restez au courant des dernières nouvelles sur nos produits et offres. S'abonner à[notre blog ici](http://blog.aspose.com).
### **Contribuer**
[](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java)

[!\[à faire:image_alt_text\]](https://s3.amazonaws.com/github/ribbons/forkme_right_red_aa0000.png)](https://github.com/AsposeShowcase/Html5_Tableur_Éditeur_par_Aspose.Cells_pour_Java)


HTML5 Spreadsheet Editor est un projet open source qui offre un maximum d'options à chacun pour contribuer au projet.

**Code source**

 La source du projet est disponible sur[GithubGenericName](https://github.com/AsposeShowcase/Html5_Spreadsheet_Editor_by_Aspose.Cells_for_Java). Nous maintenons également des miroirs Git sur les sites suivants :

- [Bitbucket](https://bitbucket.org/asposeshowcase/html5_spreadsheet_editor_by_aspose.cells_for_java)
- [SourceForge](https://sourceforge.net/p/html5-spreadsheet-editor/)

**Demandes d'extraction**

 Pour contribuer au code source du projet, envoyez simplement une pull request via Github. Lire plus d'informations dans l'article de Github sur[Créer une demande d'extraction](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).
### **Licence**
**Licence MIT**

 Nous utilisons l'une des licences open source les plus libérales pour les responsabilités minimales des contributeurs. HTML5 Spreadsheet Editor est publié sous[Licence MIT](https://opensource.org/licenses/mit-license.php).

**Aspose Licence**

 Le produit fonctionne sans licence Aspose,[avec des restrictions](/cells/fr/java/licensing/) . Pour supprimer les limitations, vous pouvez acquérir un[licence temporaire gratuite](https://purchase.aspose.com/temporary-license) ou[acheter la licence complète](https://purchase.aspose.com/buy).

 Par défaut, l'éditeur essaiera de charger**Aspose.Total.Java.lic** fichier de**src/main/resources/com/aspose/spreadsheeteditor** annuaire. Copiez simplement le fichier de licence dans ce répertoire. Le comportement par défaut peut être modifié en modifiant le**AsposeLicence** classer.
