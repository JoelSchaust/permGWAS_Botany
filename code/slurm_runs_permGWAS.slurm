#!/bin/bash
#SBATCH --job-name=permGWAS
#SBATCH --output=data/slurm_out/%x_%A_%a.out
#SBATCH --error=/data/slurm_out/%x_%A_%a.err
#SBATCH --time=02:00:00 #maximale Runtime von 2h 
#SBATCH --mem=8G
#SBATCH --cpus-per-task=4

# Vdirectories definieren
Y_DIR="/data/y_filtered_for_CORidsv2"
OUT_DIR="/results"
X_FILE="/data/Expressionsdaten_neu_2.h5"
K_FILE="/data/Cor.csv"
SINGULARITY_IMAGE="/storage/singularity_images/permgwas.sing"

# Alle Y-Dateien abrufen
Y_FILES=($Y_DIR/CORID_filtered_Y*.csv)
Y_FILE=${Y_FILES[$SLURM_ARRAY_TASK_ID-1]}  #task ID aus sbatch --array=1-$NUM_FILES slurm_runs_permGWAS_joel.slurm
Y_BASENAME=$(basename "$Y_FILE" .csv)  

# jedes output von y bekommt ein eigene Ordner
RESULT_DIR="$OUT_DIR/$Y_BASENAME"
mkdir -p "$RESULT_DIR"

# Singularity skript startn 
singularity exec --nv --bind /storage:/storage "$SINGULARITY_IMAGE" \
    python3 ~/git/permGWAS/permGWAS.py \
    -x "$X_FILE" \
    -y "$Y_FILE" \
    -k "$K_FILE" \
    -not_add \
    -perm 100 \
    -mplot \
    -out_dir "$RESULT_DIR"
