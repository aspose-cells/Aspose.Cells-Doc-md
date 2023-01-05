---
title: Mettre à jour les paramètres de police du côté client
type: docs
weight: 170
url: /fr/net/update-font-from-client-side/
---
{{% alert color="primary" %}}

Cette rubrique traite de la modification des paramètres de police côté client dans le contrôle Aspose.Cells.GridWeb.

{{% /alert %}}

Aspose.Cells GridWeb prend désormais en charge la modification des paramètres de police du côté client. Pour cela, le API propose les fonctions suivantes

- **mettre à jourCellFontStyle**: Params - r/i/b/ib pour regular/italic/bold/italic&&bold
- **mettre à jourCellFontSize**: Params - nom de la police, etc. 'Système'
- **updateCellFontName**: Paramètres - taille de la police, etc. '12pt'
- **updateCellFontColor**: Params - none/u/l/ul/ for none/underline/strikout/underline&&strikout
- **updateCellFontLine**: Params - couleur html comme #aa22ee ou nom de couleur bien connu comme vert, rouge,...
- **updateCellBackGroundColor**: Params - couleur html comme #aa22ee ou nom de couleur bien connu comme vert, rouge,...

L'extrait de code suivant illustre la modification des paramètres de police du côté client dans GridWeb.

## Exemple de code

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples.GridWeb-CSharp-Worksheets-UpdateFontFromClientSide.aspx" >}}
