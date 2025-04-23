---
title: Versionado
type: docs
weight: 40
url: /es/go-cpp/versioning/
description: Cómo instalar Aspose Cells para Go mediante C++ y crear una aplicación Hello World.
---

**github.com/aspose-cells/aspose-cells-go-cpp/v25** es una ruta de módulo de Go que especifica una versión particular de una biblioteca de terceros. Desglosemos esta ruta y expliquemos su significado:
Desglose de la Ruta del Módulo

1. **Dirección del Repositorio GitHub**: github.com/aspose-cells/aspose-cells-go-cpp

- Esta parte indica que la biblioteca está alojada en GitHub, bajo la organización o usuario aspose-cells, en el repositorio llamado aspose-cells-go-cpp.
- Aspose.Cells es un conjunto de API para manejar y manipular archivos de hojas de cálculo (como Excel).

1. **Número de Versión**: /v25

- /v25 indica que esta es la versión 24 de la biblioteca. En los Módulos de Go, se soporta la versión semántica (SemVer), donde los caminos que contienen /vN se usan para especificar explícitamente el número de la versión principal.
- Cuando la versión principal es mayor o igual a 2, el camino del módulo debe incluir el número de la versión para garantizar compatibilidad y aislamiento entre diferentes versiones principales.

### **Significado**

- **aspose-cells-go-cpp**: Este es un enlace del lenguaje Go para una biblioteca en C++, permitiéndote usar las funcionalidades de Aspose.Cells dentro de tus programas en Go para leer, escribir y manipular archivos Excel, entre otras operaciones.
- **v25**: Esto indica que estás haciendo referencia a la versión 24 de la biblioteca. Las diferentes versiones principales pueden introducir cambios incompatibles, por lo que especificar el número de versión es crucial para asegurar que tu proyecto dependa de la API y comportamiento correctos.

### **Uso**

Para usar aspose-cells-go-cpp v25 en tu proyecto en Go, necesitas añadir la siguiente línea en el archivo go.mod de tu proyecto:

```Go
require github.com/aspose-cells/aspose-cells-go-cpp/v25 v25.x.x
```

Reemplaza v25.x.x con los números específicos de la versión menor y parches, como v25.0.0. Puedes añadir y descargar automáticamente esta dependencia usando el comando go get:

```Go
go get github.com/aspose-cells/aspose-cells-go-cpp/v25@v25.x.x
```
