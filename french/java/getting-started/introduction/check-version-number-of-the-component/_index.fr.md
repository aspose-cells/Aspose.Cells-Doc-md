---
title: Vérifier le numéro de version du composant
type: docs
weight: 70
url: /fr/java/check-version-number-of-the-component/
---

{{% alert color="primary" %}} 

Dans certains cas, vous pourriez vous demander quelle version du produit vous possédez. Nous construisons souvent de nouvelles corrections (corrections de bogues pour les scénarios d'utilisation signalés) et les publions dans les forums en fonction de leurs besoins urgents. Le numéro de version se compose du numéro de version majeure, du numéro de version mineure et du numéro de version de correctif. Tous les composants définis doivent être des entiers supérieurs ou égaux à 0. Le format du numéro de version est le suivant :

majeur.mineur.correctif , nous pouvons augmenter une partie de 1 et créer une nouvelle version. En général, nous augmentons la dernière partie de 1 et créons une nouvelle correction à publier dans les forums pour les utilisateurs.

Ce document décrit certaines façons de vérifier quelle version du composant est installée sur votre système.

{{% /alert %}} 
## **Vérification du numéro de version**
### **1) De manière manuelle**
Si vous avez la version/correction de Java (Aspose.Cells for Java), vous pouvez décompresser le fichier jar de la bibliothèque Aspose.Cells, ouvrir le fichier MANIFEST avec le bloc-notes et rechercher la chaîne, c'est-à-dire "Specification-Version:" pour vérifier sa valeur.

![todo:image_alt_text](check-version-number-of-the-component_1.png)


**Figure:** Vérification du numéro de version de la correction Java
### **2) Utilisation des APIs**
Vous pouvez également utiliser les APIs suivantes pour obtenir le numéro de version du produit.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-introduction-CheckVersionNumberOfComponent-CheckVersionNumberOfComponent.java" >}}

{{< app/cells/assistant language="java" >}}
