#!/bin/bash

# Check if @sqds/cli is installed
if ! npm list -g @sqds/cli >/dev/null 2>&1; then
  echo "@sqds/cli is not installed. Installing..."
  npm install -g @sqds/cli
else
  echo "@sqds/cli is already installed."
fi

# Prompt for wallet keypair path
read -p "Enter the wallet keypair path: " WALLET_KEYPAIR_PATH

# Prompt for RPC cluster URL
read -p "Enter the RPC cluster URL: " RPC_CLUSTER_URL

# Run squads-cli and input the wallet keypair path and RPC cluster URL
echo "Running squads-cli with the provided inputs..."
squads-cli << EOF
$WALLET_KEYPAIR_PATH
y
$RPC_CLUSTER_URL
y
EOF