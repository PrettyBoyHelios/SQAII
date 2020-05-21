# Test Plan for Android Testing Suite
May 20th, 2020  
SDET: *Luis Enrique Correa Morán*

## Table of Contents

## Project Definition
Android Testing Suite is a Software Development that aims to create an in-house testing suite for some of Android's most important modules.
The testing suite is expected to guarantee the correct app behaviour for the Phone, Calculator and Settings apps. It is expected for the framework to be highly optimized, flexible and scalable to accommodate for a variety of different modules (or Apps) in the future.

## Scope
The project will cover the following areas for the described three modules of the Android ecosystem.

* Phone App  
    * Ability of performing local calls.  
    * Ability to make international calls.  
    * Ability to reach emergency numbers.  
* Calculator  
    * Correct handling of the sum, division, subtraction and multiplication operations.  
    * Correct handling of complex operations.  
    * Handling of edge cases with arithmetic errors and exceptions.  
    
* WiFi Settings  
    * Ability to perform state changes on the WiFi connectivity for a device.  

### Out of Scope
Any interaction of the aforementioned apps with external apps or devices will be left out of the testing scope. All tests must be run in app and on device.  
Also, it is important to mention that the testing suite will only cover the development of the core Android Apps in 
their 'Vanilla' version, what's often described as Pure Android versions of the apps, as OEM personalization layers may introduce screen elements that may be too 
much to generalize and create an optimized framework.

## Testing Levels
This project will focus black box testing, evaluating only the outcome of a given process. The testing suite will provide both **system** and **regression** testing to the Android core app development. As the testing framework will provide a comprehensive way of testing the work of all the components of an app, and to guarantee the app's behaviour on every release.  

## Exit Criteria
For a release to be approved and deployed, the following conditions must be met.