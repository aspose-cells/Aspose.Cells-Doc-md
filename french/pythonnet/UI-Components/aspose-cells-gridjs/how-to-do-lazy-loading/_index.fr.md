---
title: Comment faire du chargement paresseux dans GridJs  
type: docs
weight: 250
url: /fr/python-net/aspose-cells-gridjs/how-to-do-lazy-loading/
description: Cet article décrit comment implémenter le chargement paresseux dans GridJs.
keywords: GridJs, chargement paresseux, chargement à la demande,
aliases:
  - /python-net/aspose-cells-gridjs/lazy-loading/
  - /python-net/aspose-cells-gridjs/loading-on-demand/

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
```python 
       Config.set_lazy_loading(True)
```
## Définir l'URL d'action pour le chargement paresseux
par exemple :
```javascript
 const lazyLoadingUrl = "/GridJs2/LazyLoading";
 xs.setLazyLoadingUrl(lazyLoadingUrl);
```
Après que l'utilisateur clique sur une autre feuille qui n'est pas active, la requête de données sera automatiquement déclenchée par l'application de feuille de calcul 

## Implémenter l'action de chargement paresseux dans le contrôleur côté serveur
par exemple :
```python
@app.route('/GridJs2/LazyLoading', methods=['POST'])
def lazy_loading():
    sheet_name = request.form.get('name', '')
    uid = request.form.get('uid', '')
    if not sheet_name:
        return jsonify({'error': 'sheet_name is required'}), 400
    if not uid:
        return jsonify({'error': 'uid is required'}), 400

    wbj = GridJsWorkbook()
    try:

        output = io.BytesIO()
        with gzip.GzipFile(fileobj=output, mode='wb', compresslevel=9) as gzip_stream:
             wbj.lazy_loading_stream(gzip_stream,uid, sheet_name)


        response = Response(output.getvalue(), mimetype='application/json')
        response.headers['Content-Encoding'] = 'gzip'

        return response
    except Exception as e:
        return Response(str(e), status=500)
```





