---
title: Ventana del editor de fórmulas
type: docs
weight: 20
url: /es/reportingservices/formula-editor-window/
---
{{% alert color="primary" %}} 

El Editor de fórmulas le permite crear fórmulas para un informe.

{{% /alert %}} 

Para editar una fórmula en una celda de Excel Microsoft:

1. En Microsoft Excel, seleccione una celda.
1.  Abra el cuadro de diálogo Editar fórmula haciendo clic en**Editar fórmula** en la barra de herramientas.
   ([Adición de fórmulas de Reporting Services](/cells/es/reportingservices/adding-reporting-services-formulas/) recorre un ejemplo que edita una fórmula).
 El cuadro de diálogo se divide en secciones: el área de edición en la parte superior y el área de fórmula en la parte inferior. Utilice el área de fórmula para completar el área de edición.
1.  Seleccione una categoría (usuario, parámetros, campos, etc.) de la**Campos de informe** lista (la lista de la izquierda).
1.  Seleccione el tipo de la**Funciones** lista (en el medio).
1.  Seleccione una opción de la**Operadores** lista (la lista de la derecha).
1.  Hacer clic**Insertar**para agregar la expresión a la**Editar** zona.
1.  Hacer clic**Insertar** cuando la expresión es completa.
 La fórmula se inserta en la celda.

**El cuadro de diálogo Editar fórmula** 

![todo:imagen_alternativa_texto](formula-editor-window_1.png)

El cuadro de diálogo Editar fórmula se divide en secciones, que se describen a continuación.
#### **Editar área**
 Esta es el área donde crea o edita una fórmula. Cree una fórmula haciendo doble clic en cualquiera de los componentes enumerados en el**Campos de informe**, **Funciones** o**Operadores** liza. Cuando elige un componente, también se inserta la sintaxis requerida. También puede ingresar manualmente una fórmula.
#### **Área de fórmula**
El área de fórmulas contiene tres secciones, cada una de las cuales enumera la información utilizada para crear una fórmula.

- Campos de informe: la lista de la izquierda enumera todos los campos de la base de datos accesibles para el informe. También enumera las fórmulas o los grupos ya creados.
- Funciones: la lista del medio contiene funciones, procedimientos prediseñados que devuelven valores. Realizan cálculos como PROMEDIO, SUMA, CONTEO, SIN, MAYÚSCULAS, etc.
- Operadores: los "verbos de acción" utilizados en las fórmulas. Los operadores describen una operación o una acción que tiene lugar entre dos o más valores. Ejemplos de operadores: sumar, restar, menor que y mayor que etc.
#### **Control S**
El cuadro de diálogo tiene varios controles:

|**Nombre del botón** |**Descripción** |
|:- |:- |
| Deshacer| Deshace una acción.|
| Pegar| Pega una cadena de caracteres formada por los componentes enumerados en el área de fórmula en el área de edición.|
| Insertar| Toma el valor en el área de edición y lo inserta como una fórmula en una celda.|
| Salida| Cierra el Editor de fórmulas.|
{{% alert color="primary" %}} 

Temas relacionados:

- [Lista de fórmulas](/cells/es/reportingservices/formula-list/) - una lista de campos y operadores.

{{% /alert %}}
