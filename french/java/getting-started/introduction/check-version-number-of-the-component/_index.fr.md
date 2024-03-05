---
title: Vérifier le numéro de version du composant
type: docs
weight: 70
url: /fr/java/check-version-number-of-the-component/
---
{{% alert color="primary" %}} 

Dans certains cas, vous vous demandez peut-être quelle version du produit vous possédez. Souvent, nous construisons de nouveaux correctifs (corrections de bogues pour les scénarios utilisateur qu'ils signalent) et les publions dans les forums contre leur besoin urgent. Le numéro de version comprend le numéro de version majeure, le numéro de version mineure et le numéro de version du correctif. Tous les composants définis doivent être des entiers supérieurs ou égaux à 0. Le format du numéro de version est le suivant :

major.minor.hotfix , nous pouvons augmenter une partie de 1 et créer une nouvelle version. Normalement, nous augmentons la dernière partie de 1 et créons un nouveau correctif pour le publier sur les forums pour les utilisateurs.

Ce document décrit quelques façons de vérifier quelle version du composant est installée sur votre système.

{{% /alert %}} 
## **Vérification du numéro de version**
### **1) manière manuelle**
Si vous avez la version/le correctif Java (Aspose.Cells for Java), vous pouvez décompresser le fichier jar de la bibliothèque Aspose.Cells, ouvrir le fichier MANIFEST avec le bloc-notes et rechercher la chaîne, c'est-à-dire "Specification-Version :" pour vérifier sa valeur.

![tâche : image_autre_texte](check-version-number-of-the-component_1.png)


**Chiffre:** Vérification du numéro de version du correctif Java
### **2) Utiliser les API**
Vous pouvez également utiliser les API suivantes pour obtenir le numéro de version du produit.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-introduction-CheckVersionNumberOfComponent-CheckVersionNumberOfComponent.java" >}}

