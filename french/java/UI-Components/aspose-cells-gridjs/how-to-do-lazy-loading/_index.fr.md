---
title: Comment faire du chargement paresseux dans GridJs  
type: docs
weight: 250
url: /fr/java/aspose-cells-gridjs/how-to-do-lazy-loading/
description: Cet article décrit comment implémenter le chargement paresseux dans GridJs.
keywords: GridJs, chargement paresseux, chargement à la demande,
aliases:
  - /java/aspose-cells-gridjs/lazy-loading/
  - /java/aspose-cells-gridjs/loading-on-demand/

---

## à propos du chargement paresseux 
Lorsqu'on traite un fichier de feuille de calcul contenant de nombreuses feuilles, nous pouvons optimiser le processus de chargement en chargeant initialement uniquement la feuille active.

Cette stratégie garantit que la réponse JSON côté serveur ne comprend initialement que les données de la feuille activement sélectionnée.  

En conséquence, le trafic web initial est considérablement réduit, améliorant l'expérience utilisateur en minimisant les temps de chargement.  

De plus, GridJs est conçu pour répondre dynamiquement aux interactions de l'utilisateur. Plus précisément, lorsqu'un utilisateur clique sur une autre feuille,

GridJs déclenche intelligemment une requête vers le serveur pour récupérer les données spécifiquement pour cette feuille.  

Ce mécanisme de chargement à la demande réduit non seulement les transferts de données inutiles mais assure également que l'utilisateur ait toujours accès aux informations les plus à jour pour la feuille sur laquelle il travaille actuellement.  

En adoptant cette approche, nous optimisons non seulement le temps de chargement initial mais maintenons également une application réactive et efficace qui se scale bien avec le nombre croissant de feuilles dans le fichier de la feuille de calcul.

# Pour implémenter le chargement paresseux dans GridJs, les étapes sont
## Définir l'option de configuration pour le chargement paresseux
par exemple :
```java 
  Config.setLazyLoading(true);
```
## Définir l'URL d'action pour le chargement paresseux
par exemple :
```javascript
 const lazyLoadingUrl = "/GridJs2/LazyLoading";
 xs.setLazyLoadingUrl(lazyLoadingUrl);
```
Après que l'utilisateur clique sur une autre feuille qui n'est pas celle active, l'action de requête des données sera déclenchée automatiquement par l'application de tableur. 

## Implémenter l'action de chargement paresseux dans le contrôleur côté serveur
par exemple :
```java
    @PostMapping("/LazyLoading")
    public void lazyLoadingStreamJson(
            @RequestParam(value = "name", required = false) String sheetName,
            @RequestParam(value = "uid", required = false) String uid,
            HttpServletResponse response) throws IOException {

        GridJsWorkbook wbj = new GridJsWorkbook();
        response.setContentType(MediaType.APPLICATION_JSON_VALUE);
        response.setHeader(HttpHeaders.CONTENT_ENCODING, "gzip");

        try (GZIPOutputStream gzipOutputStream = new GZIPOutputStream(response.getOutputStream())) {
            try {
				wbj.lazyLoadingStream(gzipOutputStream, uid, sheetName);
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
        }
    }
```





