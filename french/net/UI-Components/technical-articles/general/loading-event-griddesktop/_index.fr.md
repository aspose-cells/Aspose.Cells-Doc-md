---
title: Événement de chargement dans GridDesktop
type: docs
weight: 1060
url: /fr/net/aspose-cells-griddesktop/loading-event
description: Cet article décrit comment utiliser l événement de chargement dans GridDesktop.
keywords: GridDesktop, événement, événement de chargement, chargement
---


## **Événement de chargement pour GridDesktop**
Le code d'exemple suivant illustre comment utiliser différents types d'événements de chargement pour GridDesktop lors de l'importation d'un fichier. Veuillez consulter le [fichier Excel d'exemple](loading-event.xlsx). 

Le fichier est protégé par mot de passe, d'abord nous essayons de l'ouvrir avec un mauvais mot de passe, puis finalement dans l'événement FailLoadFile, nous utilisons un mot de passe correct pour l'ouvrir.

![vue résultante de l'événement de chargement](loadingevent.png)
### **Code d'exemple**
{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "LoadingEvent.cs" >}}

