---
title: Ouvrir un fichier Excel sans boîte de dialogue d’ouverture, de sauvegarde ou d’annulation en utilisant Node.js via C++
linktitle: Ouvrir un fichier Excel sans boîte de dialogue Ouvrir, Enregistrer, Annuler
type: docs
weight: 150
url: /fr/nodejs-cpp/opening-excel-file-without-open-save-cancel-dialog-box/
--- 

{{% alert color="primary" %}} 

Ce document explique comment ouvrir un fichier Microsoft Excel dans un navigateur sans afficher la boîte de dialogue Ouvrir-Enregistrer-Annuler. 

Il convient de noter que la restriction de sécurité qui ne permet pas le téléchargement direct d'un fichier est imposée par Microsoft (ou d'autres fournisseurs de navigateurs), et non par Aspose. Elle est imposée pour bloquer et restreindre le téléchargement de fichiers potentiellement nocifs sur les machines locales. 

Il est risqué pour le système local du client de permettre le téléchargement sans afficher la boîte de dialogue Ouvrir-Enregistrer-Annuler pour demander le téléchargement. Il n'y a pas d'option ou de solution de contournement disponible chez Aspose car cela représenterait un très grand risque de sécurité.

{{% /alert %}} 

## **Pourquoi un risque de sécurité ?**
L'image suivante montre la boîte de dialogue Ouvrir-Enregistrer-Annuler affichée par Internet Explorer lors de la tentative de téléchargement d'un fichier.

|**La boîte de dialogue Ouvrir-Enregistrer-Annuler**| 
| :- | 
|![todo:image_alt_text](opening-excel-file-without-open-save-cancel-dialog-box_1.png)| 
Comme expliqué ci-dessus, autoriser un fichier à s’ouvrir ou à s’exécuter sur votre système sans confirmation que vous le souhaitez vraiment constitue un risque de sécurité. Certains fichiers contiennent des virus, et certains sites essaieront de télécharger des fichiers nuisibles sur votre machine sans vous en avertir. Il n’est donc pas recommandé de permettre le téléchargement de fichiers sans l’invite de téléchargement, afin que les utilisateurs puissent vérifier le fichier et sa source avant de le télécharger ou de l’exécuter. La désactivation de la boîte de dialogue de téléchargement rend le système vulnérable aux virus, aux chevaux de Troie et aux pirates informatiques qui peuvent affecter silencieusement votre système. 

## **Ouverture d'un fichier sans la boîte de dialogue Ouvrir-Enregistrer-Annuler**
Bien que ce soit un gros problème de sécurité, Microsoft propose toujours des paramètres d'Internet Explorer permettant aux utilisateurs de désactiver la demande d'ouvrir-enregistrer-annuler pour le téléchargement de fichiers. 

Dans l'Explorateur Windows :

1. Dans le menu **Outils**, sélectionnez **Options de dossier**.
1. Cliquez sur l'onglet Types de fichiers dans la boîte de dialogue Options de dossier.
1. Sélectionnez le type de fichier avec l'extension XLS.
1. Cliquez sur **Avancé**. 
   Une boîte de dialogue s'affiche. Elle propose trois options en bas.
1. Décochez **Confirmer l'ouverture après le téléchargement**.
1. Sélectionnez la troisième option - **Naviguer dans la même fenêtre** - pour afficher le fichier Excel dans Internet Explorer sans démarrer Microsoft Excel à part. 

|**Options de modification du type de fichier**| 
| :- | 
|![todo:image_alt_text](opening-excel-file-without-open-save-cancel-dialog-box_2.png)| 
Ce paramètre permet aux fichiers de s'exécuter directement dans le navigateur web, sans afficher la boîte de dialogue Ouvrir-Enregistrer-Annuler lors du téléchargement ou de l'ouverture du fichier. 
{{< app/cells/assistant language="nodejs-cpp" >}}
