---
title: Introduction de GridWeb
type: docs
weight: 10
url: /fr/java/introduction-of-gridweb/
---
##  **Bases de GridWeb**
 Aspose.Cells.GridWeb est un contrôle Web basé sur une interface graphique qui peut être intégré dans des pages Web JSP ou dans n'importe quelle page HTML du serveur Java.
{{% alert color="primary" %}} 

Il est facile et simple à utiliser.

Il vous aide à créer rapidement un éditeur Web en ligne pour un fichier de feuille de calcul.

Il prend également en charge l'importation et l'exportation de toutes sortes de fichiers au format tableur, 100 % compatibles avec les fichiers MS Excel.

##  **Aspose.Cells.GridWeb - Démos**
{{% alert color="primary" %}} 

Pour vous permettre d'être opérationnel rapidement, nous fournissons un certain nombre d'exemples de code et de démos qui montrent comment utiliser Aspose.Cells.GridWeb API.

Veuillez télécharger les démos à partir du lien ci-dessous :
[Aspose.Cells.GridWeb Démos](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridWeb)


##  **Comment exécuter Aspose.Cells pour les démos GridWeb Java**
{{% alert color="primary" %}} 

 Aspose.Cells pour les démos GridWeb Java sont faciles à exécuter. Il vous suffit de déployer**grillewebdemo.war** dans votre serveur Web. Veuillez télécharger les démos à partir de ceci[lien](https://forum.aspose.com/uploads/discourse_instance3/22292).

Cet article décrit comment exécuter Aspose.Cells pour les démos GridWeb Java sur le serveur Apache Tomcat.

{{% /alert %}} 
###  **Guide étape par étape pour exécuter les démos GridWeb Java**
1.  Extrait**apache-tomcat-7.0.52.zip** dans n'importe quel répertoire, par exemple C:\Tomcat

![tâche : image_alt_text](introduction-of-gridweb_1.png)



 L'instantané suivant montre les répertoires et fichiers extraits du serveur Apache Tomcat

![tâche : image_alt_text](introduction-of-gridweb_2.png)



 Vous devrez peut-être également définir la variable d'environnement**CATALINA_HOME** 

![tâche : image_alt_text](introduction-of-gridweb_3.png)

1.  Ouvrez le**tomcat-users.xml** déposer.

![tâche : image_alt_text](introduction-of-gridweb_4.png)

1. Ajoutez cet utilisateur :

{{< highlight "java" >}}

   <role rolename="manager-gui"/>

  <user username="tomcat" password="secret" roles="manager-gui"/>

{{< /highlight >}}



**Ici le nom d'utilisateur est Tomcat et le mot de passe est secret** 

![tâche : image_alt_text](introduction-of-gridweb_5.png)

1.  Exécutez le**démarrage.bat** déposer.
 Il exécutera le serveur Apache Tomcat.

![tâche : image_alt_text](introduction-of-gridweb_6.png)



**Serveur Tomcat s'exécutant dans une fenêtre de commande** 

![tâche : image_alt_text](introduction-of-gridweb_7.png)

1. Ouvrez maintenant le navigateur et tapez *localhost:8080**.
 La page Web Apache Tomcat s'affiche.

   **La page Web d'Apache Tomcat** 

![tâche : image_alt_text](introduction-of-gridweb_8.png)

1.  Cliquez sur**Application de gestion** et saisissez le nom d'utilisateur et le mot de passe. (Comme ci-dessus : matou, secret)

![tâche : image_alt_text](introduction-of-gridweb_9.png)

1.  Faites défiler jusqu'à la section**Fichier WAR à déployer** et parcourez le**grillewebdemo.war** déposer.
1.  Cliquez sur *Déployer**.

![tâche : image_alt_text](introduction-of-gridweb_10.png)

1. Parcourir**grillewebdemo.war** déposer.

![tâche : image_alt_text](introduction-of-gridweb_11.png)

1.  Cliquez sur *Déployer**.

![tâche : image_alt_text](introduction-of-gridweb_12.png)

1.  Une fois déployé, cliquez sur**/gridwebdemo** et commencez à exécuter des démos.

![tâche : image_alt_text](introduction-of-gridweb_13.png)


 La page de démonstration GridWeb s'affiche.

**La page de démonstration GridWeb** 

![tâche : image_alt_text](introduction-of-gridweb_14.png)

1.  Cliquez sur n’importe quelle démo et exécutez-la.

   **Démo de création de contenu en cours d'exécution** 

![tâche : image_alt_text](introduction-of-gridweb_15.png)



**Démo de feuilles de calcul en cours d'exécution** 

![tâche : image_alt_text](introduction-of-gridweb_16.png)



**Démo HeaderBar et CommandButton en cours d'exécution** 

![tâche : image_alt_text](introduction-of-gridweb_17.png)


{{% /alert %}} 
##  **Capacités des navigateurs et Aspose.Cells.GridWeb**
Aspose.Cells.GridWeb est un contrôle Web basé sur une interface graphique qui peut être intégré dans des pages Web JSP comme d'autres contrôles Web. La chose la plus importante à propos du contrôle Web est la prise en charge de plusieurs navigateurs. Aspose.Cells.GridWeb fournit une prise en charge multi-navigateurs.
###  **Comparaison**
Aspose.Cells.GridWeb est entièrement pris en charge sur Internet Explorer (IE) de Microsoft. Cependant, sur d'autres navigateurs, il présente des limitations mineures. Cette rubrique fournit une comparaison détaillée des fonctionnalités prises en charge par différents navigateurs.

|**Fonctionnalités côté client**|**Microsoft Internet Explorer**|**Google Chromé**|**Mozilla Firefox**|**Opéra**|
| :- | :- | :- | :- | :- |
|Menu contextuel du Cell|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/cross >}}|
|Validation côté client|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Événement Double-Clic|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| La liste déroulante (*Mode ComboBox* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| La liste déroulante (*Mode menu contextuel* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Entrée/Modification de formule|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Geler ou débloquer des lignes/colonnes|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| Liens hypertextes (*Mode Commande Cellulaire* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
| Liens hypertextes (*Mode URL* )|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Fusionner ou annuler la fusion Cells|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Multiple Cells Copier/Coller|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Entrée/modification multiple Cells, publication unique|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Format de nombre|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Pagination de feuille|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Lecture seule Cells|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Lignes/colonnes en lecture seule|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Validation des données à l'aide d'expressions régulières|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Redimensionner la largeur de la colonne|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Redimensionner la hauteur de la ligne|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Insérer/Supprimer des lignes et des colonnes|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Faire défiler le contenu|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Faire défiler les onglets de la feuille|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Définir les bordures de Cells|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Définir les paramètres de police de Cells|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
{{< emoticons/cross >}} Le menu contextuel d'une cellule ne peut être activé qu'en cliquant sur le bouton Menu côté client.
