<!--
.. title: Machine Learning for Seasonal Climate Forecasting
.. slug: machine-learning-for-seasonal-climate-forecasting
.. date: 2020-07-27 18:58:49 UTC+12:00
.. tags: Seasonal Forecasting, Machine Learning
.. category: Research projects
.. link: 
.. description: 
.. type: text
-->

Over the past 2 years I have been working on a project aimed at developing better (more accurate) and more locally relevant (downscaled) seasonal climate forecasts for New Zealand, using Machine Learning. In this series of posts I will present the motivation thinking behind this project, the methodological and technical solutions (and challenges) that we faced, and some preliminary results ... first I'll try and explain a few concepts. 

<!-- TEASER_END -->

## What are seasonal climate forecasts ?

While **weather forecasting** aims to provide precise, fine grained forecasts of weather parameters at specific locations for the next few days typically (e.g. *How much rainfall will fall tomorrow morning over Auckland ?*, or *What will be the maximum wind speed between 6 and 11 PM*), **Seasonal Climate Forecasting** is concerned about forecasting some kind of *aggregated statistics* over a period of one to three months, and is usually expressed in probabilistic terms, so typical statements are e.g.: *what is the probability that cumulative rainfall over the next three months period will be in the above normal range*, or *how likely is it that the average temperature for next month will be below normal*.  

Seasonal Climate Forecasts also typically valid for regions and areas rather than point locations. In New Zealand, [NIWA](http://www.niwa.co.nz) has been producing [3 months (seasonal) climate outlooks]() for rainfall, temperature, soil moisture and river flows, for 6 large regions (see figure below).  

They are called *outlooks* rather than forecasts because they are assembled - painstakingly - every month by a group of climate scientists and hydrologists, after reviewing a whole lot of material and lines of evidence, ranging the current state and recent evolution of climate indicators, to the outputs of various dynamical (General Circulation Models, ... more on that later) and statistical forecast models. These outlooks are thus derived from a mix of purely quantitative, data driven conclusions, and expert opinion, and are usually called 'consensus' outlooks. Reaching 'consensus' is sometimes a messy affair, and is a time-consuming process: Between the assembling of the material, the analysis, running some in-house statistical models and the experts' meeting itself, the few rounds of review of the final product, many hours each month are dedicated to this product. 

## General Circulation Models and seasonal climate forecasts 

**GCMs (General Circulation Models)** are basically gigantic software programs (hundreds of thousands of lines of code, usually in Fortran !) that encapsulate our knowledge of the physical processes driving the various components of the climate system, and the interaction between these components. They are - truly - a crown achievement of the scientific endeavour, and are the result of hundred of years of human-hours, built on hundred of years of development in our scientific understanding of physics, chemistry, biology, etc ...

These GCMs are routinely run every month by various international institutions, providing monthly and seasonal (usually about 9 months in advance) aggregated statistics (averages, total, minimum and maximum, etc) for a whole range of climate variables. While they are usually quite accurate in their representation of what the large-scale climate anomalies will look like (e.g. they are pretty good at predicting the El Nino Southern Oscillation several months in advance), they are not so great at predicting the details of seasonal climate anomalies over countries such as New Zealand / Aotearoa, which is relatively small, has a complex topography, and lies outside of the tropical region, where predictability is the highest. This is largely due to the spatial resolution of the GCMs being relatively coarse, because of the computational constraints of running simulation for several months in the future, as opposed to a few days for Numerical Weather Prediction models. Typical resolutions for GCMs range between 1x1 to 2.5x2.5 degrees in latitude and longitude. The topography in these GCMs is therefore very smooth compared to reality, and this leads to deficits in the representation of interactions between the large scale circulation and the topography, which is important especially for precipitation. 

