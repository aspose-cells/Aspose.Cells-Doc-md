---
title: Définir des formules  Avis aux utilisateurs non anglophones
type: docs
weight: 10
url: /fr/net/setting-formulas-notice-for-non-english-users/
---

{{% alert color="primary" %}} 

Aspose.Cells prend en charge la plupart des formules/fonctions qui font partie de Microsoft Excel. Les développeurs peuvent utiliser ces formules avec l'API ou les [feuilles de calcul conçues](/cells/fr/net/what-is-a-designer-spreadsheet/). Aspose.Cells prend en charge un ensemble énorme de formules mathématiques, de chaînes, booléennes, de date/heure, statistiques, de base de données, de recherche et de référence. Les formules doivent être spécifiées en utilisant le style anglais (États-Unis).

{{% /alert %}} 
## **Avis aux utilisateurs non anglophones**
Il y a deux conseils que les utilisateurs non anglophones doivent suivre lors de la création de formules avec Aspose.Cells :

1. Les formules doivent être saisies en anglais. Par exemple, utilisez l'anglais "=SUM()" et pas l'allemand "=SUMME()".
1. Toujours utiliser une virgule (,) pour délimiter les paramètres de fonction. Pour certaines options linguistiques ou paramètres, le délimiteur pour les paramètres de fonction est un point-virgule mais Aspose.Cells utilise le style anglais avec une virgule. Par exemple, utiliser "=SI (C5=0,0,C3/C4)" et non pas "=SI(C5=0;0;C3/C4)"
