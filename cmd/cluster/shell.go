/*
Copyright © 2023 NAME HERE <EMAIL ADDRESS>
*/
package cmd

import (
	"errors"
	"github.com/spf13/cobra"
	"virtual-cluster/service/cluster"
	"virtual-cluster/utility"
)

// cluster/shellCmd represents the shell command
var shellCmd = &cobra.Command{
	Use:   "shell",
	Short: "Connect to shell of specific node.",
	Long:  `Connect to shell of specific node.`,
	RunE: func(cmd *cobra.Command, args []string) (err error) {
		value, _ := cmd.Flags().GetString("name")

		if len(args) > 0 {
			err = errors.New("Unnecessary arguments found")
			return
		}

		// Check if multipass instance with same name is running
		// If invalid args given, return error
		if validate := utility.CheckNodeNameExist(value); !validate {
			err = errors.New(utility.CriticalMessageString("Node name not found : ", value))
			return
		}

		// Check if it's proper name
		if validate := utility.NodeNameValidater(value); !validate {
			err = errors.New("Node naming convention violated : " + value)
			return
		}

		// Check if multipass instance is kubernetes' instance
		if validate := utility.CheckIsClusterInstance(value); !validate {
			err = errors.New(utility.CriticalMessageString("'", value, "' is not a kubernetes cluster instance"))
			return
		}

		err = cluster.AddCluster(value)
		return
	},
}

func init() {
	shellCmd.Flags().StringVarP(&nodename, "name", "n", "", "Name of node you want to connect")
	addCmd.MarkFlagRequired("name")
}
