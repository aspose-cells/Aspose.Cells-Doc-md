---
title: Ouverture d'un fichier Excel sans ouvrir la boîte de dialogue d'annulation d'enregistrement
type: docs
weight: 150
url: /fr/net/opening-excel-file-without-open-save-cancel-dialog-box/
---
{{% alert color="primary" %}} 

Ce document explique comment ouvrir un fichier Excel Microsoft dans un navigateur sans afficher la boîte de dialogue Ouvrir-Enregistrer-Annuler.

 Il convient de noter ici que la restriction de sécurité qui ne permet pas le téléchargement direct d'un fichier est appliquée par Microsoft (ou d'autres fournisseurs de navigateurs), et non par Aspose. Il est imposé de bloquer et d'empêcher le téléchargement de fichiers potentiellement dangereux sur des machines locales. .

Il est risqué pour le système local du client d'autoriser le téléchargement sans afficher la boîte de dialogue Ouvrir-Enregistrer-Annuler pour demander le téléchargement. Il n'y a pas d'option ou de solution de contournement disponible à partir du Aspose car ce sera un très gros risque de sécurité.

{{% /alert %}} 
## **Pourquoi un risque de sécurité ?**
L'image suivante montre la boîte de dialogue Ouvrir-Enregistrer-Annuler affichée par Internet Explorer lors de la tentative de téléchargement d'un fichier.

|**La boîte de dialogue Ouvrir-Enregistrer-Annuler**|
|:- |
|![tâche : image_autre_texte](opening-excel-file-without-open-save-cancel-dialog-box_1.png)|
Comme expliqué ci-dessus, autoriser un fichier à s'ouvrir ou à s'exécuter sur votre système sans confirmation que vous le souhaitez vraiment constitue un risque pour la sécurité. Certains fichiers contiennent des virus et certains sites essaieront de télécharger des fichiers nuisibles sur votre ordinateur sans vous y inviter. Il n'est donc pas recommandé d'autoriser le téléchargement de fichiers sans l'invite de téléchargement afin que les utilisateurs doivent vérifier le fichier et sa source puissent être vérifiés avant de le télécharger ou de l'exécuter. La désactivation de la boîte de dialogue de téléchargement rend le système vulnérable aux virus, chevaux de Troie et pirates qui peuvent affecter silencieusement votre système.
## **Ouverture d'un fichier sans la boîte de dialogue Ouvrir-Enregistrer-Annuler**
 Bien qu'il s'agisse d'un gros problème de sécurité, Microsoft fournit toujours des paramètres Internet Explorer qui permettent aux utilisateurs de désactiver l'invite Ouvrir-Enregistrer-Annuler pour le téléchargement de fichiers.

Dans l'explorateur Windows :

1.  Sur le**Outils** menu, sélectionnez**Options de dossier**.
1. Cliquez sur l'onglet Types de fichiers dans la boîte de dialogue Options des dossiers.
1. Sélectionnez le type de fichier d'extension XLS.
1.  Cliquez sur**Avancé**. 
Une boîte de dialogue s'affiche. Il a trois options en bas.
1.  Décochez**Confirmer l'ouverture après le téléchargement**.
1.  Sélectionnez la troisième option -**Parcourir dans la même fenêtre** - pour afficher le fichier Excel dans Internet Explorer sans démarrer Microsoft Excel autonome.

|**Modification des options de type de fichier**|
|:- |
|![tâche : image_autre_texte](opening-excel-file-without-open-save-cancel-dialog-box_2.png)|
Ce paramètre permet aux fichiers de s'exécuter directement dans le navigateur Web, sans que la boîte de dialogue Ouvrir-Enregistrer-Annuler ne s'affiche lors du téléchargement ou de l'ouverture du fichier.
