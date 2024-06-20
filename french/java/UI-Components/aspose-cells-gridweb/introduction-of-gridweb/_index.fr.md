---
title: Introduction de GridWeb
type: docs
weight: 10
url: /fr/java/introduction-of-gridweb/
---
## **Fondamentaux de GridWeb**
Aspose.Cells.GridWeb est un contrôle web basé sur une interface graphique qui peut être intégré dans des pages web JSP ou toute page html en java server. 
{{% alert color="primary" %}} 

Il est facile et simple à utiliser.

Il vous aide à construire rapidement un éditeur de feuilles de calcul en ligne.

Il prend également en charge l'importation et l'exportation de tous types de fichiers de formats de feuilles de calcul qui sont 100% compatibles avec les fichiers MS Excel.

## **Aspose.Cells.GridWeb - Démos**
{{% alert color="primary" %}} 

Pour vous permettre de démarrer rapidement, nous fournissons un certain nombre d'exemples de code et de démos qui montrent comment utiliser l'API Aspose.Cells.GridWeb.

Veuillez télécharger les démos à partir du lien ci-dessous :
[Aspose.Cells.GridWeb Démos](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Examples.GridWeb)


## **Comment exécuter les démos Aspose.Cells pour GridWeb Java**
{{% alert color="primary" %}} 

Les démos Aspose.Cells pour GridWeb Java sont faciles à exécuter. Vous avez juste besoin de déployer **gridwebdemo.war** dans votre serveur Web. Veuillez télécharger les démos à partir de ce [lien](https://forum.aspose.com/uploads/discourse_instance3/22292).

Cet article décrit comment exécuter les démos Aspose.Cells pour GridWeb Java dans le serveur Apache Tomcat.

{{% /alert %}} 
### **Guide pas à pas pour exécuter les démos GridWeb Java**
1. Extraire **apache-tomcat-7.0.52.zip** dans n'importe quel répertoire, par exemple C:\Tomcat 

![todo:image_alt_text](introduction-of-gridweb_1.png)



La capture d'écran suivante montre les répertoires et fichiers extraits du serveur Apache Tomcat 

![todo:image_alt_text](introduction-of-gridweb_2.png)



Vous devrez peut-être également définir la variable d'environnement **CATALINA_HOME** 

![todo:image_alt_text](introduction-of-gridweb_3.png)

1. Ouvrir le fichier **tomcat-users.xml** 

![todo:image_alt_text](introduction-of-gridweb_4.png)

1. Ajouter cet utilisateur :

{{< highlight java >}}

   <role rolename="manager-gui"/>

  <user username="tomcat" password="secret" roles="manager-gui"/>

{{< /highlight >}}



**Ici, le nom d'utilisateur est tomcat et le mot de passe est secret** 

![todo:image_alt_text](introduction-of-gridweb_5.png)

1. Exécuter le fichier **startup.bat**
   Cela lancera le serveur Apache Tomcat. 

![todo:image_alt_text](introduction-of-gridweb_6.png)



**Serveur Tomcat en cours d'exécution dans une fenêtre de commande** 

![todo:image_alt_text](introduction-of-gridweb_7.png)

1. Ouvrez maintenant le navigateur et saisissez **localhost:8080**
   La page Web d'Apache Tomcat est affichée. 

   **La page Web Apache Tomcat** 

![todo:image_alt_text](introduction-of-gridweb_8.png)

1. Cliquez sur **Manager App** et saisissez le nom d'utilisateur et le mot de passe. (Comme ci-dessus : tomcat, secret) 

![todo:image_alt_text](introduction-of-gridweb_9.png)

1. Faites défiler vers la section **Fichier WAR à déployer** et parcourez le fichier **gridwebdemo.war**.
1. Cliquez sur **Déployer**. 

![todo:image_alt_text](introduction-of-gridweb_10.png)

1. Parcourez le fichier **gridwebdemo.war**. 

![todo:image_alt_text](introduction-of-gridweb_11.png)

1. Cliquez sur **Déployer**. 

![todo:image_alt_text](introduction-of-gridweb_12.png)

1. Une fois déployé, cliquez sur **/gridwebdemo** et lancez les démos. 

![todo:image_alt_text](introduction-of-gridweb_13.png)


La page de démonstration GridWeb est affichée. 

**La page de démonstration GridWeb** 

![todo:image_alt_text](introduction-of-gridweb_14.png)

1. Cliquez sur n'importe quelle démo et exécutez-la. 

   **Création de démonstration de contenu en cours d'exécution** 

![todo:image_alt_text](introduction-of-gridweb_15.png)



**Démo de feuilles de calcul en cours d'exécution** 

![todo:image_alt_text](introduction-of-gridweb_16.png)



**Démo de HeaderBar et CommandButton en cours d'exécution** 

![todo:image_alt_text](introduction-of-gridweb_17.png)


{{% /alert %}} 
## **Capacités des navigateurs et Aspose.Cells.GridWeb**
Aspose.Cells.GridWeb est un contrôle Web basé sur une interface graphique pouvant être intégré dans des pages Web JSP comme d'autres contrôles Web. La chose la plus importante pour le contrôle Web est de fournir une prise en charge multi-navigateurs. Aspose.Cells.GridWeb fournit une prise en charge multi-navigateurs.
### **Comparaison**
Aspose.Cells.GridWeb est entièrement pris en charge sur Internet Explorer (IE) de Microsoft. Cependant, sur d'autres navigateurs, il présente des limitations mineures. Ce sujet fournit une comparaison détaillée des fonctionnalités prises en charge par différents navigateurs.

|**Fonctionnalités côté client**|**Microsoft Internet Explorer**|**Google Chrome**|**Mozilla Firefox**|**Opera**|
| :- | :- | :- | :- | :- |
|Menu contextuel de cellule|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/cross >}}|
|Validation côté client|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Événement Double-clic| {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | 
|DropDownList (*Mode ComboBox*)| {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | 
|DropDownList (*Mode Menu contextuel*)| {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | 
|Saisie/Modification de formule| {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | 
|Geler ou dégeler lignes/colonnes| {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | 
|Hyperliens (*Mode CommandeCellule*)| {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | 
|Hyperliens (*Mode URL*)| {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | 
|Fusionner ou séparer des cellules| {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | 
|Copier/Coller de plusieurs cellules| {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | 
|Saisie/Modification de plusieurs cellules, un seul renvoi| {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | 
|Format de nombre| {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | 
|Pagination de feuille| {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | 
|Cellules en lecture seule| {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | 
|Lignes/colonnes en lecture seule| {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | 
|Validation de données en utilisant des expressions régulières| {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | 
|Redimensionner la largeur de la colonne| {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | 
|Redimensionner la hauteur de la ligne| {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | 
|Insérer/Supprimer lignes et colonnes| {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | 
|Défilement du contenu| {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | 
|Défilement des onglets de feuille| {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | {{< emoticons/tick >}} | 
|Définir les bordures des cellules|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
|Définir les paramètres de la police des cellules|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|{{< emoticons/tick >}}|
{{< emoticons/cross >}} Context menu of a cell can only be activated by clicking the Client side menu button.
