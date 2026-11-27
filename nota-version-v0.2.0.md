# Nota de versión v0.2.0

**Fecha:** 22 de noviembre de 2026

## Resumen
Esta versión introduce el patrón Observer en el componente de control de existencias del sistema del colmado, con el fin de desacoplar la actualización del stock de las acciones que se derivan de ella.

## Componente intervenido
Control de existencias y alerta de stock mínimo (RF02, RF03, RF04, RF06), representado por la clase `Producto`.

## Cambios principales
- `Producto` actúa como sujeto y notifica a sus observadores al cambiar el stock.
- `AlertaStockMinimo` muestra la alerta cuando el stock es menor o igual al mínimo definido.
- `RegistroMovimientos` guarda el historial de ventas y compras.

## Verificación
Se ejecutó `src/inventario/demo.py`: la alerta se activa únicamente cuando el stock llega al mínimo y cada movimiento queda registrado.

Posteriormente se diseñaron 27 pruebas con pytest 9.2.0 (carpeta `tests/`). La primera ejecución detectó cinco no conformidades en `Producto`, que se corrigieron en el mismo componente. La ejecución final aprobó las 27 pruebas y la demo mantuvo su resultado.

## Compatibilidad
Mantiene los atributos y el método `actualizarStock()` definidos en el diagrama de clases de la versión 0.1.0
