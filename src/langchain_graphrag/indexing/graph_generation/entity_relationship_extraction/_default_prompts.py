# ruff: noqa

DEFAULT_ER_EXTRACTION_PROMPT = """
-Goal-
Given a text document related to scikit-learn documentation and a list of entity types, identify all entities of those types from the text and all relationships among the identified entities.

-Steps-
1. Identify all entities. For each identified entity, extract the following information:
   - entity_name: Name of the entity, capitalized (e.g., "RANDOMFORESTCLASSIFIER")
   - entity_type: One of the following types: [{entity_types}]
         * Estimator: Classes for building predictive models (e.g., LogisticRegression, RandomForestClassifier)
         * Transformer: Classes for transforming data (e.g., StandardScaler, PCA)
         * Method: Methods of classes (e.g., fit, predict, transform)
         * Parameter: Hyperparameters and constructor parameters (e.g., n_estimators, C)
         * Attribute: Model attributes obtained after training (e.g., coef_, feature_importances_)
         * Metric: Metrics for evaluating models (e.g., accuracy_score, mean_squared_error)
         * Dataset: Datasets used in examples (e.g., iris, digits)
         * Task: Machine learning tasks (e.g., classification, regression, clustering)
         * Module: Submodules of the library (e.g., sklearn.model_selection, sklearn.metrics)
         * Exception: Exceptions and errors raised by the library (e.g., NotFittedError)
         * Concept: Core concepts and methodologies (e.g., cross-validation, regularization)
   - entity_description: A comprehensive description of the entity, detailing its attributes, functionality, and role within scikit-learn.
Format each entity as ("entity"{tuple_delimiter}<entity_name>{tuple_delimiter}<entity_type>{tuple_delimiter}<entity_description>)

2. From the entities identified in step 1, identify all pairs of (source_entity, target_entity) that are *clearly related* to each other.
   For each pair of related entities, extract the following information:
   - source_entity: Name of the source entity, as identified in step 1.
   - target_entity: Name of the target entity, as identified in step 1.
   - relationship_description: Explanation why the source entity and target entity are related (e.g., a method belonging to an estimator, a parameter associated with a specific model, or a module that contains a particular transformer).
   - relationship_strength: A numeric score indicating the strength of the relationship between the source and target entities.
Format each relationship as ("relationship"{tuple_delimiter}<source_entity>{tuple_delimiter}<target_entity>{tuple_delimiter}<relationship_description>{tuple_delimiter}<relationship_strength>)

3. Return the output in English as a single list of all the entities and relationships identified in steps 1 and 2. Use **{record_delimiter}** as the list delimiter.

4. When finished, output {completion_delimiter}

######################
-Examples-
######################
Example 1:
Entity_types: Estimator,Method,Parameter,Module
Text:
The RandomForestClassifier in sklearn.ensemble is a popular estimator that implements methods such as fit and predict. Its parameter n_estimators controls the number of trees in the ensemble.
######################
Output:
("entity"{tuple_delimiter}RANDOMFORESTCLASSIFIER{tuple_delimiter}ESTIMATOR{tuple_delimiter}A classifier that builds an ensemble of decision trees, located in sklearn.ensemble)
{record_delimiter}
("entity"{tuple_delimiter}FIT{tuple_delimiter}METHOD{tuple_delimiter}A method used to train the RandomForestClassifier on the input data)
{record_delimiter}
("entity"{tuple_delimiter}PREDICT{tuple_delimiter}METHOD{tuple_delimiter}A method used to generate predictions after training)
{record_delimiter}
("entity"{tuple_delimiter}N_ESTIMATORS{tuple_delimiter}PARAMETER{tuple_delimiter}A parameter that defines the number of trees in the RandomForestClassifier)
{record_delimiter}
("entity"{tuple_delimiter}SKLEARN.ENSEMBLE{tuple_delimiter}MODULE{tuple_delimiter}A submodule of scikit-learn that provides ensemble-based estimators)
{record_delimiter}
("relationship"{tuple_delimiter}RANDOMFORESTCLASSIFIER{tuple_delimiter}FIT{tuple_delimiter}The 'fit' method is implemented by the RandomForestClassifier to train the model{tuple_delimiter}8)
{record_delimiter}
("relationship"{tuple_delimiter}RANDOMFORESTCLASSIFIER{tuple_delimiter}PREDICT{tuple_delimiter}The 'predict' method is used by RandomForestClassifier for inference after training{tuple_delimiter}8)
{record_delimiter}
("relationship"{tuple_delimiter}RANDOMFORESTCLASSIFIER{tuple_delimiter}N_ESTIMATORS{tuple_delimiter}The parameter 'n_estimators' configures the number of trees in the RandomForestClassifier{tuple_delimiter}7)
{record_delimiter}
("relationship"{tuple_delimiter}RANDOMFORESTCLASSIFIER{tuple_delimiter}SKLEARN.ENSEMBLE{tuple_delimiter}The RandomForestClassifier is defined in the module sklearn.ensemble{tuple_delimiter}9)
{completion_delimiter}

Example 2:
Entity_types: Transformer,Method,Parameter,Concept
Text:
StandardScaler is a transformer that standardizes features by removing the mean and scaling to unit variance. It implements the fit and transform methods and includes parameters such as with_mean and with_std. This process is an example of feature scaling.
######################
Output:
("entity"{tuple_delimiter}STANDARDSCALER{tuple_delimiter}TRANSFORMER{tuple_delimiter}A transformer that standardizes features by removing the mean and scaling to unit variance)
{record_delimiter}
("entity"{tuple_delimiter}FIT{tuple_delimiter}METHOD{tuple_delimiter}A method used to compute the necessary statistics (mean and standard deviation) for scaling data)
{record_delimiter}
("entity"{tuple_delimiter}TRANSFORM{tuple_delimiter}METHOD{tuple_delimiter}A method used to apply the scaling transformation to the data based on computed statistics)
{record_delimiter}
("entity"{tuple_delimiter}WITH_MEAN{tuple_delimiter}PARAMETER{tuple_delimiter}A parameter that indicates whether to center the data before scaling)
{record_delimiter}
("entity"{tuple_delimiter}WITH_STD{tuple_delimiter}PARAMETER{tuple_delimiter}A parameter that indicates whether to scale data to unit variance)
{record_delimiter}
("entity"{tuple_delimiter}FEATURE SCALING{tuple_delimiter}CONCEPT{tuple_delimiter}A core concept in data preprocessing that involves standardizing features)
{record_delimiter}
("relationship"{tuple_delimiter}STANDARDSCALER{tuple_delimiter}FIT{tuple_delimiter}StandardScaler uses the 'fit' method to compute mean and standard deviation for scaling{tuple_delimiter}9)
{record_delimiter}
("relationship"{tuple_delimiter}STANDARDSCALER{tuple_delimiter}TRANSFORM{tuple_delimiter}StandardScaler applies the 'transform' method to standardize the data based on computed statistics{tuple_delimiter}9)
{record_delimiter}
("relationship"{tuple_delimiter}STANDARDSCALER{tuple_delimiter}WITH_MEAN{tuple_delimiter}The 'with_mean' parameter controls whether the data is centered before scaling{tuple_delimiter}7)
{record_delimiter}
("relationship"{tuple_delimiter}STANDARDSCALER{tuple_delimiter}WITH_STD{tuple_delimiter}The 'with_std' parameter controls whether the data is scaled to unit variance{tuple_delimiter}7)
{record_delimiter}
("relationship"{tuple_delimiter}STANDARD SCALING{tuple_delimiter}FEATURE SCALING{tuple_delimiter}The process implemented by StandardScaler is an example of feature scaling in data preprocessing{tuple_delimiter}8)
{completion_delimiter}

######################
-Real Data-
######################
Entity_types: {entity_types}
Text: {input_text}
######################
Output:
"""
