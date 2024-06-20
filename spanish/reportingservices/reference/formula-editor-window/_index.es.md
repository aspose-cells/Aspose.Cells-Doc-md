---
title: Ventana del Editor de Fórmulas
type: docs
weight: 20
url: /es/reportingservices/formula-editor-window/
---

{{% alert color="primary" %}} 

El Editor de Fórmulas le permite crear fórmulas para un informe.

{{% /alert %}} 

Para editar una fórmula en una celda de Microsoft Excel:

1. En Microsoft Excel, seleccione una celda.
1. Abre el diálogo Editar Fórmula haciendo clic en **Editar Fórmula** en la barra de herramientas.
   ([Agregar fórmulas de Servicios de Informes](/cells/es/reportingservices/adding-reporting-services-formulas/) muestra un ejemplo que edita una fórmula.)
   El diálogo está dividido en secciones: el área de edición en la parte superior y el área de fórmula en la parte inferior. Utiliza el área de fórmula para poblar el área de edición.
1. Selecciona una categoría (usuario, parámetros, campos, etc.) de la lista **Campos de Informe** (la lista de la izquierda).
1. Selecciona el tipo de la lista **Funciones** (en el medio).
1. Selecciona una opción de la lista **Operadores** (la lista de la derecha).
1. Haz clic en **Insertar** para agregar la expresión al área **Editar**.
1. Haz clic en **Insertar** cuando la expresión esté completa.
   La fórmula se inserta en la celda.

**El diálogo Editar Fórmula** 

![todo:image_alt_text](formula-editor-window_1.png)

El diálogo Editar Fórmula está dividido en secciones, descritas a continuación.
#### **Área de Edición**
Esta es el área donde creas o editas una fórmula. Crea una fórmula haciendo doble clic en cualquiera de los componentes listados en las listas **Campos de Informe**, **Funciones** u **Operadores**. Cuando eliges un componente, la sintaxis requerida también se inserta. También puedes ingresar manualmente una fórmula. 
#### **Área de Fórmula**
El área de fórmula contiene tres secciones, cada una enumera información utilizada para construir una fórmula.

- Campos de Informe - la lista de la izquierda enumera todos los campos de la base de datos accesibles para el informe. También lista cualquier fórmula o grupo ya creados.
- Funciones - la lista del medio contiene funciones, procedimientos predefinidos que devuelven valores. Realizan cálculos como PROMEDIO, SUMA, CONTAR, SEN, MAYÚSCULAS, etc.
- Operadores - los 'verbos de acción' utilizados en fórmulas. Los operadores describen una operación o una acción que se lleva a cabo entre dos o más valores. Ejemplos de operadores: sumar, restar, menor que y mayor que, etc.
#### **Controles**
El diálogo tiene varios controles:

|**Nombre del botón** |**Descripción** |
| :- | :- |
|Undo |Deshace una acción. |
|Paste |Pega una cadena de caracteres compuesta por los componentes enumerados en el área de fórmulas en el área de edición. |
|Insert |Toma el valor en el área de edición y lo inserta como una fórmula en una celda. |
|Exit |Cierra el Editor de fórmulas. |
{{% alert color="primary" %}} 

Temas relacionados:

- [Lista de Fórmulas](/cells/es/reportingservices/formula-list/) - una lista de campos y operadores.

{{% /alert %}}
