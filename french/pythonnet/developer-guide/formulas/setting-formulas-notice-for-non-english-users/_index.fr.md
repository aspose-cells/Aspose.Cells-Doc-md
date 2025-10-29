---
title: Définir des formules  Avis aux utilisateurs non anglophones
type: docs
weight: 10
url: /fr/python-net/setting-formulas-notice-for-non-english-users/
---

{{% alert color="primary" %}} 

Aspose.Cells pour Python via .NET supporte la plupart des formules/fonctions qui font partie de Microsoft Excel. Les développeurs peuvent utiliser ces formules avec l'API ou [les feuilles de calcul de conception](/cells/fr/net/what-is-a-designer-spreadsheet/). Aspose.Cells pour Python via .NET supporte un vaste ensemble de formules mathématiques, de chaînes, booléennes, date/heure, statistiques, base de données, recherche et référence. Les formules doivent être spécifiées en utilisant le style anglais (US).

{{% /alert %}} 

## **Avis aux utilisateurs non anglophones**
Il y a deux astuces que les utilisateurs non anglophones doivent suivre lors de la création de formules avec Aspose.Cells pour Python via .NET :

1. Les formules doivent être saisies en anglais. Par exemple, utilisez l'anglais "=SUM()" et pas l'allemand "=SUMME()".
1. Utilisez toujours une virgule (,) pour délimiter les paramètres de la fonction. Pour certaines options ou réglages linguistiques, le délimiteur pour les paramètres de fonction est un point-virgule, mais Aspose.Cells pour Python via .NET utilise la virgule du style anglais. Par exemple, utilisez "=IF (C5=0,0,C3/C4)" et non "=IF(C5=0;0;C3/C4)"

{{< app/cells/assistant language="python-net" >}}
